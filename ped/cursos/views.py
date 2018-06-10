from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso, Inscricao
from .forms import ContataCurso
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):

    curso = Curso.objects.all()
    template_name = 'cursos/index.html'
    context = {
        'cursos': curso
    }
    return render(request, template_name, context)


def details(request, slug):

    curso = get_object_or_404(Curso, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContataCurso(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(curso)
            form = ContataCurso()
    else:
        form = ContataCurso()

    context['cursos'] = curso
    context['form'] = form
    template_name = 'cursos/details.html'
    return render(request, template_name, context)


@login_required
def inscricao(request, slug):

    curso = get_object_or_404(Curso, slug=slug)
    inscricao, created = Inscricao.objects.get_or_create(
        user=request.user,
        curso=curso
    )

    if created:
        inscricao.active()
        messages.sucess(request, 'Você foi inscrito no curso com sucesso')
    else:
        messages.info(request, 'Você já está inscrito no curso')    

    return redirect('user:dashboard')
