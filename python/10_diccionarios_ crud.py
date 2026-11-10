droides = [
    {
        "codigo": "B1-001",
        "Modelo": "B1",
        "Energia": 90,
        "Activo": True
    },
    {
        "codigo": "B1-002",
        "Modelo": "B1",
        "Energia": 40,
        "Activo": False
    },
    {
        "codigo": "DRO-001",
        "Modelo": "Droideka",
        "Energia": 80,
        "Activo": True
    },
]
# Contar
cantidad_droides = len(droides)
print(cantidad_droides)
nuevo_droide = {
    "codigo": "B1-004",
    "Modelo": "B1",
    "Energia": 80,
    "Activo": True
}
# Crud
# Crear
droides.append(nuevo_droide)
print(len(droides))
print(droides)
# Leer
droide = droides[2]
print(f"Codigo: {droide["codigo"]}")
print(f"Modelo: {droide["Modelo"]}")
print(f"Enegeria: {droide["Energia"]}")
print(f"Activo: {droide["Activo"]}")
# Actualizar
droide = droides[2]
droide["codigo"] = "DRO-002"
droide["Energia"] = 85
droide["activo"] = False
print(f"droides: {droides}")
# Eliminar
eliminado = droides.pop(2)
print(f"droides: {droides}")
