class Androide: 
    nombre: str
    energia: str
    def __init__(self, nombre: str, energia: int):
        self.nombre = nombre
        self.energia = energia
    def mostrar_energia(self):
        print("Androide", self.nombre)
        print("Energia:", self.energia)

class AndroideRecargable(Androide):
    def __init__(self, nombre: str, energia: int):
        super().__init__(nombre, energia)

    def recargar(self, cantidad: int):
        if cantidad > 0:
            self.energia += cantidad
androide17 = AndroideRecargable("Androide 17", 600)
print("===== ANTES DE RECARGAR =====")
androide17.mostrar_energia()
androide17.recargar(100)
print("===== DESPUES DE RECARGAR =====")
androide17.mostrar_energia()