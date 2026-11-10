from django.urls import path
from catalogo.views.libro_views import create_libro, libro_list

urlpatterns = [
    path('libros/', libro_list, name='libro_list'),
    path('libros/crear/', create_libro, name='create_libro'),
]
