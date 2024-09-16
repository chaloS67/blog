
from django.views.generic.list import ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
import post
from post.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home_view(request):
    posteo = Post.objects.all()
    return render(request,'home.html',{post: post})

class CrearPost(LoginRequiredMixin,CreateView):

    model = Post
    fields = ['titulo','contenido']
    template_name = 'crear_post.html'
    success_url= reverse_lazy ('home')

def form_valid(self, form):
        form.instance.autor = self.request.user  # Establecer el usuario actual como el autor
        return super().form_valid(form)


class RegistroUsuario(CreateView):
    template_name = 'registro.html'  
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class PosteoListView(ListView):
    model = Post
    context_object_name = 'post'  # Nombre del contexto en la plantilla






