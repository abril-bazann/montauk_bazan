from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    first_name= forms.CharField(max_length=50)
    last_name= forms.CharField(max_length=50)
    website=forms.URLField(label="Link a tu website")
    frase=forms.CharField(max_length=255, label="Frase de tu película favorita")
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'website', 'frase']
        help_texts = {k:"" for k in fields}


class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")