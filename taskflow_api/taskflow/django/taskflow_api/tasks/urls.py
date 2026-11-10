from django.urls import path
from . import views
from .views import lista, task_create

app_name = "tasks"

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("saludo", views.saludo, name="saludo"),
    path("greeting/<str:nombre>/",
          views.greeting, name="greeting"),
    path("destination/<str:titulo>/<str:nombre>/<str:cargo>",
              views.destination, name="destinatario"),
    path("base_triangulo/<int:base>/<int:altura>",
                  views.base_triangulo, name="base_triangulo"),
    path("my_first_template", views.my_first_template, name="my_first_template"),
    path("leads-like", views.leads_like, name="leads-like"),
    path("task/lista", views.lista, name="task-lista"),
    path("project", views.projects_list, name="projects-list"),
    path("projects/new/", views.project_create, name="project_create"),
    path("task/new/", views.task_create, name="task_create"),
    
]

