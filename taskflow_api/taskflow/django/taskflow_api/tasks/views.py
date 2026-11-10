from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import TaskForm, ProjectForm
from .models import Project

def home(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("Hola, TaskFlow")

def register(request):
    """Resgistro de usuarios."""
    return HttpResponse("Registro de usuarios en linea")

def saludo(request):
    """Saludo a usuarios."""
    return HttpResponse("Bienvenido usuario, te saluda el creador")

def greeting(request, nombre):
    """Saludo a usuarios con entrada."""
    return HttpResponse(f"Hola {nombre}, bienvenido a TaskFlow")

def destination(request, titulo, nombre, cargo):
    """Saludo a usuarios."""
    return HttpResponse(f"bienvenido: {titulo} {nombre}, su cargo es: {cargo}")

def base_triangulo(request, base, altura):
    """Saludo a usuarios."""
    return HttpResponse(f"La base es: {base*altura/2}")

def my_first_template(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    }
    return render(request, "tasks/my-first-template.html", contexto)

def home(request):
    return HttpResponse("""
        <html>
            <body>
                <h1>TaskFlow</h1>
                <p>Bienvenido al sistema</p>
            </body>
        </html>
    """)

def leads_like(request):
    contexto = {
        "titulo": "Piloto",
        "nombre": "Nicolas",
        "apellido": "Romero"
    }
    return render(request, "leads/leads-like.html", contexto)

def lista(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
        "projects": Project.objects.order_by("-created_at"),
    }
    return render(request, "home.html", contexto)

def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:projects-list") 
    else:
        form = ProjectForm() 

    return render(request, "tasks/project_form.html", {"form": form, "modo": "crear"})

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:home")
    else:
            form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form, "modo": "crear"})

def projects_list(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
        "projects": Project.objects.order_by("-created_at"),
    }
    return render(request, "tasks/projects.html", contexto)


