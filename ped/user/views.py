from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.conf import settings
from .forms import RegisterForm, EditAccountForm


def dashboard(request):
    template_name = 'user/dashboard.html'
    return render(request, template_name)


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

def edit(request):
    template_name = 'user/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
    context ['form'] = form
    return render(request, template_name, context)

def edit_password(request):
    template_name = 'user/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)