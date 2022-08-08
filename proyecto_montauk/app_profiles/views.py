from django.shortcuts import render
import email
from wsgiref.util import request_uri
from django.shortcuts import render
from django.urls import reverse_lazy
from app_profiles.models import Avatar
from django.http import HttpResponse
from django.template import Context, Template, loader
from datetime import datetime
import datetime
from app_profiles.forms import UserEditForm, AvatarForm 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
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
            return render(request, 'inicio.html', {'usuario':request.user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE'})
    else:
        formulario=AvatarForm()
    return render(request, 'agregar_avatar.html', {'formulario':formulario, 'usuario':request.user})

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
            return render(request, 'inicio.html', {'usuario':usuario, 'mensaje':'PERFIL EDITADO EXITOSAMENTE'})
    #en caso de q no sea post
    else:
        #creo form con los datos que voy a modificar
        formulario=UserEditForm(instance=usuario)
    return render(request, 'editar_perfil.html', {'formulario':formulario, 'usuario':usuario.username})
