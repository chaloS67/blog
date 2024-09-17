
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PostForm
from post.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home_view(request):
    post = Post.objects.all()
    return render(request,'home.html',{post: post})

class CrearPost(LoginRequiredMixin,CreateView):

    form_class = PostForm
    template_name = 'crear_post.html'
    success_url= reverse_lazy ('home')

def form_valid(self, form):
            post = form.save(commit=False)
            post.autor = self.request.user
            post.save()
            return super().form_valid(form)

class ListarPost(ListView):
    model = Post
    context_object_name = 'posts'  # Nombre del contexto en la plantilla
    template_name = 'listar_post.html'  # Nombre de la plantilla

    def get_queryset(self):
        # Filtra los posts del usuario autenticado
        return Post.objects.filter(autor=self.request.user)

class RegistroUsuario(CreateView):
    template_name = 'registro.html'  
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class EliminarPost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name ='eliminar_post.html'
    success_url = reverse_lazy('listar_post')









