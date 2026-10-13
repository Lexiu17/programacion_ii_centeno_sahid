"""
Control de naves
"""
naves = [
    {"nombre": "Naboo-1", 
     "combustible": 45, 
     "droides": ["R2-D2", "R2-A6"]
     },
    {"nombre": "Caza Real", 
     "combustible": 35, 
     "droides": ["R5-D4"]
     },
    {"nombre": "Transporte", 
     "combustible": 65, 
     "droides": ["M-5"]
     }
]

naves_listas = 0
naves_recarga = 0
total_droides = 0
total_ciclos = 0


for numero, nave in enumerate(naves, start=1):
    print(f"----Nave: {numero}-{nave}")
    if nave["combustible"] >= 50:
        print("Estado incial: LISTA")
        naves_listas += 1
    else:
        print("Estado incial: RECARGA")
        naves_recarga += 1
        ciclo=0
        while nave["combustible"] <=50:
            ciclo+=1
            nave["combustible"] += 10
        total_ciclos += ciclo
        print("recarga completada")
        print("Estado final: LISTA")
    total_droides = len(nave["droides"])
    for droide in nave ["droides"]:
        print(f"droide: {droide}")

print("=================================")
print("RESUMEN")
print("=================================")
print(f"Total naves: {len(naves)}")
print(f"Naves listas: {naves_listas}")
print(f"Naves recargadas: {naves_recarga}")
print(f"Total droides: {total_droides}")
print(f"Total ciclos: {total_ciclos}")