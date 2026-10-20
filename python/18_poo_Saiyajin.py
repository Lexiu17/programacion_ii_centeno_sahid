from poo_Guerrero import Guerrero #Importamos la clase padre

class Saiyajin(Guerrero): #Clase hija tiene un inicializador que llama al inicializador de la clase padre
    def __init__(self, nombre: str):
        super().__init__(nombre)

    def transformarse(self):
        print(self.nombre, "Se transforma en SuperSaiyajin")

goku = Saiyajin("Goku")
goku.presentarse()
goku.transformarse()

