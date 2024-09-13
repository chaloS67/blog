from django.shortcuts import render
from django.views.generic.edit import CreateView
from post.models import Post
# Create your views here.

def home_view(request):
    return render(request,'home.html')

class CrearPost(CreateView):

    model = Post
    fields = ['titulo','contenido']
    template_name = 'crear_post.html'
    


