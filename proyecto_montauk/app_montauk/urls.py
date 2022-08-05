from unicodedata import name
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('about/', about, name= 'about'),
    path('ver_posts/', ver_posts, name= 'ver_posts'),
    path('post/', post, name= 'post'),
    path('contact/', contact, name= 'contact'),
    path('posts_viejos/', posts_viejos, name= 'posts_viejos'),
    
    #path('post_formulario/', post_formulario, name= 'post_formulario'),
#-------------------
    path('login/', login_request, name= 'login'),
    path('register/', register, name= 'register'),
    path('logout/', LogoutView.as_view(template_name="app_montauk/logout.html"), name= 'logout'),
    path('editar_perfil/', editar_perfil, name= 'editar_perfil'),
    path('agregar_avatar/', agregar_avatar, name= 'agregar_avatar'),
#------------------
    path('post/list/', post_list.as_view(), name= 'List'),
    path('post/<pk>/', post_detalle.as_view(), name= 'Detail'),
    path('post/list/nuevo/', post_creacion.as_view(), name= 'Create'),
    path('post/editar/<pk>', post_update.as_view(), name= 'Edit'),
    path('post/borrar/<pk>', post_delete.as_view(), name= 'Delete'),
    
]