from django.urls import path
from . import views
from django.contrib.auth.views import login as authLogin
app_name = 'user'

urlpatterns = [
    path('entrar',
         authLogin,
         {'template_name': 'user/login.html'},
         name='login',
         ),

    path('registrar',
         views.registrar,
         name='register',
         ),
]
