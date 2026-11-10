from django.urls import path

from . import views
from .views import tasks

app_name = "tasks"

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("about-me", views.about_me, name="about_me"),
    path("saludo", views.saludo, name="saludo"),
    path("greeting/<str:nombre>/",
          views.greeting, name="greeting"),
    path("destination/<str:titulo>/<str:nombre>/<str:cargo>",
              views.destination, name="destinatario"),
    path("base_triangulo/<int:base>/<int:altura>",
                  views.base_triangulo, name="base_triangulo"),
    path("my-first-template/", views.my_first_template, name="my-first-template"),
    path("leads-like/", views.leads_like, name="leads_like"),
    path("project/crear/", tasks.project_create, name="project_crear"),
    path("proyects", tasks.proyect_lista, name="proyect_lista"),
    path("proyects/new/", tasks.project_create, name="project_new"),
    path("task/<int:task_id>/editar", tasks.task_edit, name="task_editar"),
]

