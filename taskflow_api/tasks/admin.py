from django.contrib import admin
from .models import Biblioteca, Comida, Nave, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Nave)
class NaveAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Comida)
class ComidaAdmin(admin.ModelAdmin):
    list_display = ("nombre_comida", "categoria", "created_at")
    search_fields = ("nombre_comida", "categoria")
    list_filter = ("categoria",)


@admin.register(Biblioteca)
class BibliotecaAdmin(admin.ModelAdmin):
    list_display = ("nombre_libro", "categoria", "created_at")
    search_fields = ("nombre_libro", "categoria")
    list_filter = ("categoria",)