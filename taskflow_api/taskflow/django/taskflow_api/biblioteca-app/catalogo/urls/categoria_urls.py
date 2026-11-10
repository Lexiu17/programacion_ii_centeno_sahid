from django.urls import path
from catalogo.views.categoria_views import (
     categoria_create,
     categoria_delete,
     categoria_list,
     categoria_update,
)

urlpatterns = [
    path('categorias/', 
         categoria_list,
          name='categoria_list'),   
    path('categorias/crear/',
         categoria_create,
         name='categoria_create'),
    path('categorias/<int:categoria_id>/editar/',
         categoria_update,
         name='categoria_update'),
    path('categorias/<int:categoria_id>/eliminar/',
         categoria_delete,
         name='categoria_delete'),
    
]