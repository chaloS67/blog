from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

   
    titulo = models.TextField()
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.titulo