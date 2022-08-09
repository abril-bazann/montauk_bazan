from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)


class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    frase=models.CharField(max_length=255)
    website=models.URLField()

    def __str__(self):
        return str(self.user)