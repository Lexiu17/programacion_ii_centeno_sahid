
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogo.urls.home_url')),
    path('catalogo/',
         include('catalogo.urls.categoria_urls')),
    path('catalogo/',
         include('catalogo.urls.libro_urls')),
]
