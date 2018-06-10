from django.template import Library
from ped.cursos.models import Inscricao

register = Library()


@register.inclusion_tag('cursos/templatetags/meus_cursos.html')
def meus_cursos(user):
    inscricoes = Inscricao.objects.filter(user=user)
    context = {
        'inscricao': inscricoes
    }
    return context

@register.simple_tag()
def load_meus_cursos(user):
    return Inscricao.objects.filter(user=user)