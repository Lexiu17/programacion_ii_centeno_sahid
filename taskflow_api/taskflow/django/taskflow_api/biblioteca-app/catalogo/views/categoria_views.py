from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from catalogo.forms.categoria_form import CategoriaForm
from catalogo.models import Categoria

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(
        request,
        'catalogo/categorias/categoria_list.html',
        {'categorias': categorias},
    )
                                                                                                                                                                                                                                                                     
def categoria_create(request):
    if request.method=='POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente.')
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(
        request,
        'catalogo/categorias/formulario.html',
        {'form': form},
    )

def categoria_update(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente.')
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(
        request,
        'catalogo/categorias/formulario.html',
        {'form': form},
    )

def categoria_delete(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada exitosamente.')
        return redirect('categoria_list')
    return render(
        request,
        'catalogo/categorias/categoria_confirm_delete.html',
        {'categoria': categoria},
    )