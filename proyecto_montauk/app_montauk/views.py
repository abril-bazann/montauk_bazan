from django.shortcuts import render
import email
from wsgiref.util import request_uri
from django.shortcuts import render
from django.urls import reverse_lazy
from app_montauk.models import Avatar, Blog
from django.http import HttpResponse
from django.template import Context, Template, loader
from datetime import datetime
import datetime
from app_montauk.forms import UserRegisterForm, UserEditForm, AvatarForm #Blog_form
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, "app_montauk/inicio.html")

def ver_posts(request):
    return render(request, "app_montauk/ver_posts.html")

def posts_viejos(request):
    return render(request, "app_montauk/posts_viejos.html")

def about(request):
    return render(request, "app_montauk/about.html")

def post(request):
    return render(request, "app_montauk/post.html")

def contact(request):
    return render(request, "app_montauk/contact.html")

def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid:
            client=request.POST ['username']
            clave=request.POST ['password']

            usuario= authenticate(username=client, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "app_montauk/inicio.html", {"mensaje":f"Hola {usuario} !"})
            else:
                return render(request, "app_montauk/inicio.html", {"mensaje":"Error; datos incorrectos"})
        else:
            return render(request, "app_montauk/inicio.html", {"mensaje":"Error; formulario erroneo"})
    form= AuthenticationForm()
    return render(request, "app_montauk/login.html", {"form":form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]

            form.save()
            return render(request, 'app_montauk/inicio.html', {'form':form,'mensaje':f"Usuario Creado:  {username}"})
    else:
        form = UserRegisterForm()
    return render(request, 'app_montauk/registro.html', {'form': form})

def post(request):
    return render(request, "app_montauk/post_detalle.html")

@login_required
def editar_perfil(request):
    usuario=request.user
    #si es metodo post hago lo mismo que al agregar
    if request.method == 'POST':
        formulario=UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            #datos que se modifican
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()
            return render(request, 'app_montauk/inicio.html', {'usuario':usuario, 'mensaje':'PERFIL EDITADO EXITOSAMENTE'})
    #en caso de q no sea post
    else:
        #creo form con los datos que voy a modificar
        formulario=UserEditForm(instance=usuario)
    return render(request, 'app_montauk/editar_perfil.html', {'formulario':formulario, 'usuario':usuario.username})


#saco uno y pongo otro
def agregar_avatar(request):
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatar_viejo=Avatar.objects.get(user=request.user)
            if(avatar_viejo.imagen):
                avatar_viejo.delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'app_montauk/inicio.html', {'usuario':request.user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE'})
    else:
        formulario=AvatarForm()
    return render(request, 'app_montauk/agregar_avatar.html', {'formulario':formulario, 'usuario':request.user})


class post_list(ListView, LoginRequiredMixin):
    model=Blog
    template_name="app_montauk/post_list.html"

class post_detalle(DetailView, LoginRequiredMixin):
    model= Blog
    template_name= "app_montauk/post_detalle.html"

class post_creacion(CreateView, LoginRequiredMixin):
    model=Blog
    success_url= reverse_lazy('List') #reverse_lazy: a donde va a ir cuando termine la creacion
    fields=['titulo', 'subtitulo','cuerpo', 'autor', 'fecha', 'imagen']

class post_update(UpdateView, LoginRequiredMixin):
    model=Blog
    success_url= reverse_lazy('List') #reverse_lazy: a donde va a ir cuando termine la creacion
    fields=['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']

class post_delete(DeleteView, LoginRequiredMixin):
    model=Blog
    success_url= reverse_lazy('List') 
    fields=['titulo', 'subtitulo','cuerpo', 'autor', 'fecha', 'imagen']