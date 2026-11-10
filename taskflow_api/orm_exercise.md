##primero importamos 
-----from tasks.models import Biblioteca

##Despues ver los objetos del modelo o clase
-----Biblioteca.objects.all()
<QuerySet []>

##Creamos una fila
----Biblioteca.objects.create(
... nombre_libro="La bella durmiente",
... categoria="Fantasia",
... descripcion="Entregado martes 27"
... )
<Biblioteca: La bella durmiente>

##crear de manera mas rapida 
----p = Biblioteca(nombre_libro="Los 3 Cerditos",categoria="Fantasia", descripcion="Entregada lunes 26")
----p.save()

##Obtener una sola fila 
----Biblioteca.objects.get(nombre_libro="Cenicienta")
<Biblioteca: Cenicienta>

##por id
----Biblioteca.objects.get(pk=1)
<Biblioteca: La bella durmiente>

##Filtar por nombres
----Biblioteca.objects.filter(nombre_libro="Blanca nieves")
<QuerySet [<Biblioteca: Blanca nieves>]>

##Exclir por su nombre
----Biblioteca.objects.exclude(nombre_libro="Cenicienta")
<QuerySet [<Biblioteca: La bella durmiente>, <Biblioteca: Los 3 Cerditos>, <Biblioteca: Blanca nieves>]>

##inexistente
----Biblioteca.objects.filter(nombre_libro="Pinocho")
<QuerySet []>

##Filtrado pero por condiciones
##Texto sensible mayusculas
----Biblioteca.objects.filter(nombre_libro__contains="el")
<QuerySet [<Biblioteca: La bella durmiente>, <Biblioteca: el lobo feroz>]>

##Texto Sensible mayusculas
----Biblioteca.objects.filter(nombre_libro__icontains="CENICIENTA")
<QuerySet [<Biblioteca: Cenicienta>]>

##Filto para empezar o terminar
----Biblioteca.objects.filter(nombre_libro__startswith="el")
<QuerySet [<Biblioteca: el lobo feroz>]>

##Filtro Fechas
----from datetime import date
----Biblioteca.objects.filter(created_at__gte=date(2026, 1, 1))
<QuerySet [<Biblioteca: La bella durmiente>, <Biblioteca: Los 3 Cerditos>, <Biblioteca: Cenicienta>, <Biblioteca: Blanca nieves>, <Biblioteca: el lobo feroz>]>

##Descripcion 
----Biblioteca.objects.filter(descripcion__isnull=True)
<QuerySet []>

##Lista de valores
----