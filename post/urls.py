
from django.urls import path
from .views import CrearPost, home_view,ListarPost,EliminarPost,DetallePost,EditarPost

urlpatterns = [
    path('', home_view, name='home'),
    path('crear/', CrearPost.as_view(), name='crear_post'),
    path('listar/', ListarPost.as_view(), name='listar_post'),
    path('eliminar/<int:pk>/', EliminarPost.as_view(), name='eliminar_post'),
    path('detalle/<int:pk>', DetallePost.as_view(), name='detalle_post'),
    path('editar/<int:pk>,', EditarPost.as_view(), name ='editar_post')
   ]
