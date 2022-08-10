from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Blog_form(forms.Form):
    titulo= forms.CharField(max_length=50)
    subtitulo= forms.CharField(max_length=50)
    cuerpo= forms.CharField(widget=forms.Textarea) 
    autor= forms.CharField(max_length=50) 
    fecha=forms.DateField()
    imagen_blog= forms.ImageField(label="Imagen", required=False)

class Pelicula_form(forms.Form):
    nombre= forms.CharField(max_length=50)
    anio= forms.IntegerField(label="año de lanzamiento")
    sinopsis=forms.CharField(widget=forms.Textarea)
    director= forms.CharField(max_length=50) 
    ver=forms.URLField(max_length=50)
    poster= forms.ImageField(label="poster", required=False)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    first_name= forms.CharField(max_length=50)
    last_name= forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

