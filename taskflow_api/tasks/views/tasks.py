# tasks/views.py
from django.shortcuts import get_object_or_404, redirect, render

from ..forms import ProjectForm, TaskForm
from ..models import Project, Task


def proyect_lista(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
        "tasks": Task.objects.select_related("project").order_by("-created_at"),
        "projects": Project.objects.order_by("-created_at"),
    }
    return render(request, "tasks/project/projects.html", contexto)


def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:home")
    else:
        form = ProjectForm()

    return render(request, "tasks/project/project_form.html", {
        "form": form,
        "modo": "crear",
    })


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("tasks:task_lista")
    else:
        form = TaskForm()

    return render(request, "tasks/task/task_form.html", {"form": form, "modo": "crear"})


def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:task_lista")
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/task/task_form.html", {"form": form, "modo": "editar"})