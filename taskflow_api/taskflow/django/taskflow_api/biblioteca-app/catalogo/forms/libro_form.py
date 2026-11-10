from django import forms

from catalogo.models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'isbn', 'fecha_publicacion', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ISBN (opcional)',
            }),
            'fecha_publicacion': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
            ),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }
