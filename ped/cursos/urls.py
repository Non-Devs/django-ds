from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.details, name='details'),
    path('<slug:slug>/inscricao', views.inscricao, name='inscricao'),
    path('<slug:slug>/cancelar', views.undo_inscricao, name='undo_inscricao'),
    path('<slug:slug>/anuncios', views.anuncios, name='anuncios'),

]
