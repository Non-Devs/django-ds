
from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.ForumView.as_view(), name='index'),
    path('tag/<tag>', views.ForumView.as_view(), name='index_tagged'),
    path('respostas/<pk>/correta', views.ReplyCorrectView.as_view(), name='reply_correct'),
    path('respostas/<pk>/incorreta', views.ReplyCorrectView.as_view(correct=False), name='reply_incorrect'),
    path('<slug:slug>', views.ThreadView.as_view(), name='thread'),


]
