from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    titulo= models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    cuerpo= models.TextField() 
    autor= models.CharField(max_length=50) 
    fecha=models.DateField()
    imagen= models.ImageField(upload_to='imagen_blog', null=True, blank=True)

    def __str__(self):
        return self.titulo+" - "+self.autor

class Pelicula(models.Model):
    nombre= models.CharField(max_length=50)
    anio= models.IntegerField()
    director= models.CharField(max_length=50) 
    ver=models.URLField(max_length=50)
    poster= models.ImageField(upload_to='poster_pelicula', null=True, blank=True)

    def __str__(self):
        return self.nombre+" - "+self.director+" - "+self.anio

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)

