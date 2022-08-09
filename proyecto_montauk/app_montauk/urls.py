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
    
#-------------------
    
#------------------
    path('pages/', post_list.as_view(), name= 'List'),
    path('pages/<pk>/', post_detalle.as_view(), name= 'Detail'),
    path('pages/nuevo/', post_creacion.as_view(template_name="blog_form.html"), name= 'Create'),
    path('post/editar/<pk>', post_update.as_view(template_name="blog_form.html"), name= 'Edit'),
    path('post/borrar/<pk>', post_delete.as_view(template_name="blog_confirm_delete.html"), name= 'Delete'),
    
]