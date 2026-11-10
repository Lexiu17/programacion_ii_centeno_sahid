# Programación 2

Repositorio con los trabajos, ejercicios y proyectos de la materia **Programación 2**, donde se trabajan tres tecnologías: **Python**, **Odoo** y **Django**.

---

## Estructura actual

```text
.
├── python/                         # Ejercicios independientes de Python
├── taskflow_api/                   # Proyecto Django TaskFlow
│   ├── manage.py
│   ├── tasks/                       # Aplicación de tareas y proyectos
│   └── taskflow/django/taskflow_api/
│       ├── tasks/                   # Otra copia/proyecto de TaskFlow
│       └── biblioteca-app/          # Proyecto Django de biblioteca
│           ├── manage.py
│           ├── catalogo/            # Categorías, formularios y vistas
│           └── config/              # Configuración Django
└── README.md
```

Las carpetas `taskflow_api/` y `taskflow_api/taskflow/django/taskflow_api/` contienen proyectos Django separados. Cada uno tiene su propio `manage.py`; ejecuta los comandos desde la carpeta del proyecto que quieras usar. No hay actualmente carpetas `odoo/` ni un `requirements.txt` en la raíz.

## Requisitos

- Python compatible con la versión de Django indicada en cada proyecto.
- `pip`.

La app de biblioteca declara sus dependencias en `taskflow_api/taskflow/django/taskflow_api/biblioteca-app/requirements.txt`.

## Cómo ejecutar

Ejecuta un ejercicio de Python desde la raíz:

```bash
python python/01_hello_world.py
```

Para iniciar TaskFlow:

```bash
cd taskflow_api
python -m pip install Django
python manage.py migrate
python manage.py runserver
```

Para iniciar la app de biblioteca, instala sus dependencias y entra en su carpeta:

```bash
python -m pip install -r taskflow_api/taskflow/django/taskflow_api/biblioteca-app/requirements.txt
cd taskflow_api/taskflow/django/taskflow_api/biblioteca-app
python manage.py migrate
python manage.py runserver
```

En ambos casos, Django inicia por defecto en `http://127.0.0.1:8000`.

---

## Autor

**Alexander**
Estudiante de Desarrollo de Software, Universidad Tecnológica Equinoccial (UTE)

---

## Licencia

Proyecto con fines académicos.
