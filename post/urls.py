
from django.urls import path
from .views import CrearPost, PosteoListView, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('', PosteoListView.as_view()),
    path('crear/', CrearPost.as_view(), name='crear_post')

   ]
