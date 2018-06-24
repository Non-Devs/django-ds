from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.details, name='details'),
    path('<slug:slug>/inscricao', views.inscricao, name='inscricao'),
    path('<slug:slug>/undo_inscricao', views.undo_inscricao, name='undo_inscricao'),
    path('<slug:slug>/anuncios', views.anuncios, name='anuncios'),
    path('<slug:slug>/licao', views.licoes, name='licoes'),
    path('<slug:slug>/licao/<pk>', views.licao, name='licao'),
    path('<slug:slug>/material/<pk>', views.material, name='material'),
    path('<slug:slug>/anuncios/<pk>', views.exibir_anuncio, name='exibir_anuncio'),

]
