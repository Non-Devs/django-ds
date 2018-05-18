from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

app_name = 'user'

urlpatterns = [
    path('entrar',
         login,
         {'template_name': 'user/login.html'},
         name='login',
         ),

    path('sair',
         logout,
         {'next_page': 'core:home'},
         name='logout',
         ),

    path('registrar',
         views.registrar,
         name='register',
         ),
]
