from django.shortcuts import redirect, render

from catalogo.forms.libro_form import LibroForm
from catalogo.models import Libro

def libro_list(request):
    libros = Libro.objects.all()
    return render(
        request,
        'catalogo/categorias/libro/libro_list.html',
        {'libros': libros},
    )

def create_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm()
    return render(
        request,
        'catalogo/categorias/libro/libro_form.html',
        {'form': form},
    )