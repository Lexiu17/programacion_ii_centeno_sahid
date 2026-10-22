from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "task_proyect"

    def __str__(self):
        return self.name

class Nave(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "task_Nave"

    def __str__(self):
        return self.name

class Comida(models.Model):
    nombre_comida = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    ingredientes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "task_Comida"

    def __str__(self):
        return self.nombre_comida

class Biblioteca(models.Model):
    nombre_libro = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "task_Biblioteca"

    def __str__(self):
        return self.nombre_libro