from django.shortcuts import render
import email
from wsgiref.util import request_uri
from django.shortcuts import render
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.template import Context, Template, loader
from datetime import datetime
import datetime
from registro.forms import UserRegisterForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]

            form.save()
            return render(request, 'index.html', {'form':form,'mensaje':f"Usuario Creado:  {username}"})
    else:
        form = UserRegisterForm()
    return render(request, 'registro.html', {'form': form})