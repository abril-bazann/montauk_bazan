from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")