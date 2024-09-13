
from django.urls import path
from .views import CrearPost, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('crear/', CrearPost.as_view(), name="crear_post")
]
