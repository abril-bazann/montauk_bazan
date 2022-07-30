from unicodedata import name
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('about/', about, name= 'about'),
    path('post/', post, name= 'post'),
    path('contact/', contact, name= 'contact'),
#-------------------
    path('login/', login_request, name= 'login'),
    path('register/', register, name= 'register'),
    path('logout/', LogoutView.as_view(template_name="app_montauk/logout.html"), name= 'logout'),
    path('editar_perfil/', editar_perfil, name= 'editar_perfil'),
    path('agregar_avatar/', agregar_avatar, name= 'agregar_avatar'),
    
]