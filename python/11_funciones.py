## Funciones
#funciones sin parametros
def activar_sistema():
    print("==sistema de naboo==")
    print("sistema de control activado")

activar_sistema()

#funciones con parametros
def saludar_jedi(nom):
    print(f" Que la fuerza te acopañe: {nom}")

saludar_jedi("Qui-Gon Jim")
saludar_jedi("Obi-Wan Kenobi")

def mostar_nave(nombre, combustible):
    print(f"Nave: {nombre}")
    print(f"Cantidad de combustible: {combustible}")

mostar_nave("Caza N-1", 80)

#Funciones que devuelven dato o informacion
#retorno
def calcular_combustible(inicial, consumo):
    restante = inicial - consumo 
    return restante

resultado = calcular_combustible(100, 25)
print(f"Combustible: {resultado}")

def calcular_combustible2(inicial, consumo):
    return inicial - consumo

resultado = calcular_combustible2(100, 35)
print(f"Combustible: {resultado}")

print(f"combustible: {calcular_combustible2(100, 35)}")


