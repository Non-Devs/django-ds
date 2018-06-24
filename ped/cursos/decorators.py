from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .models import Curso, Inscricao


def enrollment_required(view_func):
    def _wrapper(request, *args, **kwargs):
        slug = kwargs['slug']
        curso = get_object_or_404(Curso, slug=slug)
        has_permission = request.user.is_staff
        if not has_permission:
            try:
                inscricao = Inscricao.objects.get(
                    user=request.user, curso=curso
                )
            except Inscricao.DoesNotExist:
                message = 'Desculpe, mas você não tem permissão para acessar esta página'
            else:
                if inscricao.is_approved():
                    has_permission = True
                else:
                    message = 'A sua inscrição no curso ainda está pendente'
        if not has_permission:
            messages.error(request, message)
            return redirect('accounts:dashboard')
        request.curso = curso
        return view_func(request, *args, **kwargs)
    return _wrapper
