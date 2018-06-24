from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso, Inscricao, Anuncio, Lição, Material
from .forms import ContataCurso, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import enrollment_required

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
        messages.success(request, 'Você foi inscrito no curso com sucesso')
    else:
        messages.info(request, 'Você já está inscrito no curso')    

    return redirect('user:dashboard')

@login_required
def undo_inscricao(request, slug):
    curso = get_object_or_404(Curso, slug=slug)
    inscricao = get_object_or_404(
        Inscricao,
        user=request.user,
        curso=curso
    )
    if request.method == 'POST':
        inscricao.delete()
        messages.success(request,'Sua inscrição foi cancelada!')
        return redirect('user:dashboard')
    template = 'cursos/undo_inscricao.html'
    context = {
        'inscricao': inscricao,
        'curso': curso,
    }
    return render(request, template, context)


@login_required
@enrollment_required
def anuncios(request, slug):
    curso = request.curso
    template = 'cursos/anuncios.html'
    context = {
        'curso': curso,
        'anuncios': curso.anuncios.all()
    }
    return render(request, template, context)


@login_required
@enrollment_required
def exibir_anuncio(request, slug, pk):
    curso = request.curso
    form = CommentForm(request.POST or None)
    anuncios = get_object_or_404(curso.anuncios.all(), pk=pk)
    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.user = request.user
        comentario.anuncio = anuncios
        comentario.save()
        form = CommentForm()
        messages.success(request, 'Seu comentário foi enviado com sucesso')
    template = 'cursos/exibir_anuncio.html'
    context = {
        'curso': curso,
        'anuncio': anuncios,
        'form': form,
    }
    return render(request, template, context)


@login_required
@enrollment_required
def licoes(request, slug):
    curso = request.curso
    template = 'cursos/licoes.html'
    licoes = curso.release_lessons()
    if request.user.is_staff:
        licoes = curso.licoes.all()
    context = {
        'curso': curso,
        'licoes': licoes
    }
    return render(request, template, context)


@login_required
@enrollment_required
def licao(request, slug, pk):
    curso = request.curso
    licao = get_object_or_404(Lição, pk=pk, curso=curso)
    if not request.user.is_staff and not licao.is_avaliable():
        messages.error(request, 'Esta aula não está dispoível')
        return redirect('cursos;licoes', slug=curso.slug)
    template = 'cursos/licao.html'
    context = {
        'curso': curso,
        'licao': licao
    }
    return render(request, template, context)


@login_required
@enrollment_required
def material(request, slug, pk):
    curso = request.curso
    material = get_object_or_404(Material, pk=pk, licao__curso=curso)
    licao = material.licao
    if not request.user.is_staff and not licao.is_avaliable():
        messages.error(request, 'Esta material não está dispoível')
        return redirect('cursos;licao', slug=curso.slug, pk=licao.pk)
    if not material.is_embedded():
        return redirect(material.file.url)
    template = 'cursos/material.html'
    context = {
        'curso': curso,
        'licao': licao,
        'material': material
    }
    return render(request, template, context)
