from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, \
    SetPasswordForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset
from ped.core.utils import generate_hash_key
from django.contrib import messages
from ped.cursos.models import Inscricao

User = get_user_model()


@login_required
def dashboard(request):
    template_name = 'user/dashboard.html'
    context = {}
    context['inscricao'] = Inscricao.objects.filter(user=request.user)
    return render(request, template_name, context)


def registrar(request):
    template_name = 'user/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username,
                password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('core:home')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }

    return render(request, template_name, context)


def password_reset(request):
    template_name = 'user/password_reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,
                         'Sua senha foi resetada com sucesso')
        return redirect('user:dashboard')

    context['form'] = form
    return render(request, template_name, context)


def password_reset_confirm(request, key):
    template_name = 'user/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,
                         'Sua senha foi resetada com sucesso')
        return redirect('user:dashboard')
    context['form'] = form
    return render(request, template_name, context)


@login_required
def edit(request):
    template_name = 'user/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Os dados da sua conta foram ajustados com sucesso')
            return redirect('user:dashboard')
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def edit_password(request):
    template_name = 'user/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Sua senha foi alterada com sucesso')
            return redirect('user:dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)
