from django.shortcuts import render, get_object_or_404
from .models import Curso
from .forms import ContataCurso


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
