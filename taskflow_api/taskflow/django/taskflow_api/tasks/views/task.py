# tasks/views.py
from django.shortcuts import get_object_or_404, redirect, render

from ..forms import TaskForm
from ..models import Project, Task


