from django.shortcuts import render
import email
from wsgiref.util import request_uri
from django.shortcuts import render
from django.urls import reverse_lazy
from app_montauk.models import Blog, Pelicula
from django.http import HttpResponse
from django.template import Context, Template, loader
from datetime import datetime
import datetime
from app_montauk.forms import UserRegisterForm, UserEditForm, Pelicula_form #Blog_form
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def ver_posts(request):
    return render(request, "ver_posts.html")

def posts_viejos(request):
    return render(request, "posts_viejos.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def pelicula(request):
    return render(request, "pelicula.html")

def post_img(request):
    imagen_blog=Blog.objects.filter(user= request.user.id)[0].imagen_blog.url
    img=Blog.objects.all()
    return render(request, "post.html", {"img":img, "imagen_blog":imagen_blog})

def post(request):
    return render(request, "post_detalle.html")


#-------------------- POSTS CRUD
class post_list(ListView, LoginRequiredMixin):
    model=Blog
    template_name="post_list.html"

class post_detalle(DetailView, LoginRequiredMixin):
    model= Blog
    template_name= "post_detalle.html"

class post_creacion(CreateView, LoginRequiredMixin):
    model=Blog
    success_url= reverse_lazy('List') #reverse_lazy: a donde va a ir cuando termine la creacion
    fields=['titulo', 'subtitulo','cuerpo', 'autor', 'fecha', 'imagen_blog']

class post_update(UpdateView, LoginRequiredMixin):
    model=Blog
    success_url= reverse_lazy('List') #reverse_lazy: a donde va a ir cuando termine la creacion
    fields=['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen_blog']

class post_delete(DeleteView, LoginRequiredMixin):
    model=Blog
    success_url= reverse_lazy('List') 
    fields=['titulo', 'subtitulo','cuerpo', 'autor', 'fecha', 'imagen_blog']


#---------------- PELICULAS CRUD

class pelicula_detalle(DetailView, LoginRequiredMixin):
    model= Pelicula
    template_name= "pelicula_detail.html"

class pelicula_creacion(CreateView, LoginRequiredMixin):
    model=Pelicula
    success_url= reverse_lazy('leer_peliculas') #reverse_lazy: a donde va a ir cuando termine la creacion
    fields=['nombre', 'anio', 'sinopsis','director', 'ver', 'poster']

class pelicula_update(UpdateView, LoginRequiredMixin):
    model=Pelicula
    success_url= reverse_lazy('leer_peliculas') #reverse_lazy: a donde va a ir cuando termine la creacion
    fields=['nombre', 'anio', 'sinopsis','director', 'ver', 'poster']

class pelicula_delete(DeleteView, LoginRequiredMixin):
    model=Pelicula
    success_url= reverse_lazy('leer_peliculas') 
    fields=['nombre', 'anio', 'sinopsis','director', 'ver', 'poster']


#-------------------- PELICULAS
def leer_peliculas(request):
    peliculas= Pelicula.objects.all()
    return render(request, "leer_peliculas.html", {"peliculas":peliculas})

