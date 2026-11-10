#string cadena de caracteres
jedi = "Qui-Gon Jinn"
aprendiz = "Obi-Wan Kenobi"
droide = "R2-D2"
planeta = "Naboo"
codigo = "327"

print("El jedi es: " + jedi)
print("El jedi", type(jedi))
print("El aprendiz es: " + aprendiz)
print("El aprendiz", type(aprendiz))
print("El droide es: " + droide)
print("El droide", type(droide))
print("El planeta es: " + planeta)
print("El planeta", type(planeta))
print("El código es: " + codigo)
print("El código", type(codigo))

longitud_jedi = len(jedi)
print("La longitud del nombre del jedi es:", str(longitud_jedi))

longitud_aprendiz = len(aprendiz)
print("La longitud del nombre del aprendiz es:", str(longitud_aprendiz))

longitud_droide = len(droide)
print("La longitud del nombre del droide es:", str(longitud_droide))

longitud_planeta = len(planeta)
print("La longitud del nombre del planeta es:", str(longitud_planeta))

longitud_codigo = len(codigo)
print("La longitud del código es:", str(longitud_codigo))

mensaje = "La Federación de Comercio ha impuesto un bloqueo comercial a Naboo"
print("El mensaje es: " + mensaje)
mensaje_mayusculas = mensaje.upper()
print("El mensaje en mayúsculas es: " + mensaje_mayusculas)
mensaje_minusculas = mensaje.lower()
print("El mensaje en minúsculas es: " + mensaje_minusculas)

comundicado = "Los Jedi son enviados a Naboo"
print("El comundicado es: " + comundicado)
nuevo_comundicado = comundicado.replace("Naboo", "Tatooine")
print("El nuevo comundicado es: " + nuevo_comundicado)

planetas = "Naboo, Tatooine, Coruscant, Alderaan"
planetas_lista = planetas.split(", ")
print(planetas_lista)
print("La lista de planetas es:", str(planetas_lista))
print("El primer planeta es:", planetas_lista[0])

droide = "R2-D2"
print("El droide es: " + droide)
print("El primer caracter del droide es:", droide[0])
print("El segundo caracter del droide es:", droide[1])
print("El tercer caracter del droide es:", droide[2])
print("El cuarto caracter del droide es:", droide[3])
print("El quinto caracter del droide es:", droide[4])
print("El sexto caracter del droide es:", droide[-1])

planeta = "     Naboo      "
print("El planeta es: " + planeta)
print("El planeta sin espacios en blanco es: " + planeta.strip())