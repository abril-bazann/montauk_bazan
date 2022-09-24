from django.shortcuts import render
import email
from wsgiref.util import request_uri
from django.shortcuts import render
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.template import Context, Template, loader
from datetime import datetime
import datetime

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid:
            client=request.POST ['username']
            clave=request.POST ['password']

            usuario= authenticate(username=client, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "index.html", {"mensaje":f"Hola {usuario} !"})
            else:
                return render(request, "index.html", {"mensaje":"Error; datos incorrectos"})
        else:
            return render(request, "index.html", {"mensaje":"Error; formulario erroneo"})
    form= AuthenticationForm()
    return render(request, "login.html", {"form":form})
