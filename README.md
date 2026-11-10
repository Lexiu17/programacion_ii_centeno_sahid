# Programación 2

Repositorio con los trabajos, ejercicios y proyectos de la materia **Programación 2**, donde se trabajan tres tecnologías: **Python**, **Odoo** y **Django**.

---

<<<<<<< HEAD
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
=======
## Tecnologías

### Python
Lenguaje de programación de alto nivel, interpretado y de sintaxis sencilla. Se usa para automatización, análisis de datos, desarrollo web, inteligencia artificial y mucho más. Es la base de las otras dos tecnologías de este repositorio.

### Odoo
Sistema ERP (planificación de recursos empresariales) de código abierto, escrito en Python. Permite gestionar ventas, inventario, contabilidad, compras y otros procesos de una empresa mediante módulos que se pueden personalizar o crear desde cero.

### Django
Framework web de Python que sigue el patrón MVT (Modelo-Vista-Plantilla). Incluye ORM, panel de administración, autenticación y seguridad listos para usar, lo que permite construir aplicaciones web completas de forma rápida y ordenada.

---

## Estructura del repositorio

```
programacion-2/
├── python/      # Ejercicios y prácticas de Python
├── odoo/        # Módulos y prácticas de Odoo
├── django/      # Proyectos y prácticas de Django
└── README.md
```

---

## Requisitos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Git
- PostgreSQL (necesario para Odoo)

---

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/programacion-2.git
cd programacion-2
```

2. Crear y activar un entorno virtual:

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. Instalar las dependencias de la práctica que vayas a usar:

```bash
pip install -r requirements.txt
```

---

## Cómo ejecutar

**Python**

```bash
python python/nombre_del_archivo.py
```

**Django**

```bash
cd django/nombre_del_proyecto
>>>>>>> 378acc3d337ff8c45492e399c5c027a1a1ed2108
python manage.py migrate
python manage.py runserver
```

<<<<<<< HEAD
Para iniciar la app de biblioteca, instala sus dependencias y entra en su carpeta:

```bash
python -m pip install -r taskflow_api/taskflow/django/taskflow_api/biblioteca-app/requirements.txt
cd taskflow_api/taskflow/django/taskflow_api/biblioteca-app
python manage.py migrate
python manage.py runserver
```

En ambos casos, Django inicia por defecto en `http://127.0.0.1:8000`.
=======
Luego abrir `http://127.0.0.1:8000` en el navegador.

**Odoo**

```bash
python odoo-bin -c odoo.conf
```

Luego abrir `http://localhost:8069` en el navegador.
>>>>>>> 378acc3d337ff8c45492e399c5c027a1a1ed2108

---

## Autor

**Alexander**
Estudiante de Desarrollo de Software, Universidad Tecnológica Equinoccial (UTE)

---

## Licencia

Proyecto con fines académicos.
