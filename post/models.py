from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.TextField()
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.titulo