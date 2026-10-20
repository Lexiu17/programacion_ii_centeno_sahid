#ciclo for

naves= [
    "Caza N-1",
    "Nave real de Naboo",
    "trasporte"
]
for nave in naves:
    print(f"inspecionando {nave}")

print("fin de la inspección de naves")

rondas = range(1,6)
print(f"Tipo de rondas: {type(rondas)}")
for ronda in rondas:
    print(f"Ronda de inspección: {ronda}")
    print(f"tipo de dato ronda: {type(ronda)}")


droides = range(1,17,2)
print(f"Tipo de droides: {type(droides)}")
for droid in droides:
    print(f"Droide de vigilancia: {droid}")
    print(f"tipo de dato droid: {type(droid)}")

planetas = ["Naboo", 
            "Tatooine", 
            "Coruscant", 
            "Alderaan"]

recorrido = enumerate(planetas, start=1)

for posicion, planeta in recorrido:
    print(f"Destino {posicion}: {planeta}")
    print(f"tipo de dato {type(posicion)}: {type(planeta)}")

paises = [
    "Ecuador",
    "Colombia",
    "Uruguay",
    "Chile",
    "Brasil",
    "Estados Unidos",
]

for pais in paises:
    if pais == "Chile":
        continue
    if pais == "Brasil":
        break
    print(f"Pais visitado: {pais}")

jedi = {}
print(jedi)
jedi_activo = {
    "nombre": "obi-wan",
    "fuerza": 120,
    "estilo_pelea": "samurai",
    "mision": ["guerra alderaan", "secuestro palpatine", "escolta leia"],
    "descripcion": {
        "estatura": 1.82,
        "especie": "humano",
    }
}

print(jedi_activo)
nave = dict(nombre="AZ-1", capacidad=0, turbo_laser=2)
print(nave)

jedi["nombre"] = "Luck"
jedi["fuerza"] = 150
print(jedi)

for clave, valor in jedi_activo.items():
    print(f"Clave: {clave} - Valor: {valor}")
    