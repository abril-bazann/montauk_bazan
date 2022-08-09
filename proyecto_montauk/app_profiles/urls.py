from unicodedata import name
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('agregar_avatar/', agregar_avatar, name= 'agregar_avatar'),
    path('accounts/editar_perfil/', editar_perfil, name= 'editar_perfil'),
    path('accounts/profile/', perfil, name= 'perfil'),
]