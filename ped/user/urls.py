from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

app_name = 'user'

urlpatterns = [
    path('',
         views.dashboard,
         name='dashboard',
         ),

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

    path('nova-senha',
         views.password_reset,
         name='password_reset',
         ),

    path('confirmar-nova-senha/<key>/',
         views.password_reset_confirm,
         name='password_reset_confirm',
         ),

    path('editar',
         views.edit,
         name='edit',
         ),

    path('editar-senha',
         views.edit_password,
         name='edit_password',
         ),
]
