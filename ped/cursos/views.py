from django.shortcuts import render
from .models import Curso

def index(request):

    curso=Curso.objects.all()
    template_name='cursos/index.html'
    context={
        'cursos': curso
    }
    return render(request, template_name, context)
