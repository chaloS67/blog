from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from post.models import Post
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home_view(request):
    return render(request,'home.html')

class CrearPost(CreateView):

    model = Post
    fields = ['titulo','contenido']
    template_name = 'crear_post.html'

class RegistroUsuario(CreateView):
    template_name = 'registro.html'  
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class SalirSesion(CreateView):
    template_name ='logout.html'
    success_url = reverse_lazy('home')





