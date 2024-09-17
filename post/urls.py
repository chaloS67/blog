
from django.urls import path
from .views import CrearPost, home_view,ListarPost,EliminarPost

urlpatterns = [
    path('', home_view, name='home'),
    path('crear/', CrearPost.as_view(), name='crear_post'),
    path('listar/', ListarPost.as_view(), name='listar_post'),
    path('eliminar/<int:pk>/', EliminarPost.as_view(), name='eliminar_post')
   ]
