from django.contrib import admin
from .models import Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha')  # Campos a mostrar en la lista
    search_fields = ('titulo', 'contenido')      # Campos para buscar

