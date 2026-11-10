from django.contrib import admin
from .models import Project, Animal, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Animal)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("raza", "fecha", "edad", "tamano")
    search_fields = ("edad", "raza")

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "due_date")
    list_filters = ("status","project" )
    search_fields = ("tittle","description" )