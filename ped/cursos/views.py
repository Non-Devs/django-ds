from django.shortcuts import render, get_object_or_404
from .models import Curso

def index(request):

    curso=Curso.objects.all()
    template_name='cursos/index.html'
    context={
        'cursos': curso
    }
    return render(request, template_name, context)


def details(request, slug):

    curso = get_object_or_404(Curso, slug=slug)
    context = {
        'cursos': curso
    }
    template_name = 'cursos/details.html'
    return render(request, template_name, context)