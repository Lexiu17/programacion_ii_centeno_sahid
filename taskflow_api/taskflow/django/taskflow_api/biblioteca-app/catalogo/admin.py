from django.contrib import admin

from catalogo.models import Libro


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn', 'fecha_publicacion', 'categoria')
