
class RadarDragon:
    region1: int
    region2: int

    def __init__(self, region1, region2):
        self.region1 = region1
        self.region2 = region2

    def buscar_esferas1(self, cantidad):
        esferas1 = self.region1 * cantidad
        print("Esferas encontradas en region1:", self.region1)
        print("Esferas:", esferas1)

    def buscar_esferas2(self, cantidad):
        esferas2 = self.region2 * cantidad
        print("Esferas encontradas en region2:", self.region2)
        print("Esferas:", esferas2)


radar_bulma = RadarDragon(3, 2)

radar_bulma.buscar_esferas1(1)
radar_bulma.buscar_esferas2(1)
print()

class AlmacenSemillas:
    def __init__(self, cantidad):
        self.__cantidad = cantidad
    
    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.__cantidad = nueva_cantidad

    def entregar_semillas(self, cantidad):
        if cantidad <= self.__cantidad:
            self.__cantidad = self.__cantidad - cantidad
            print("Se entregaron", cantidad, "semillas")
        else:
            print("No hay suficientes semillas. Solo quedan", self.__cantidad)


almacen = AlmacenSemillas(10)

print("Entregar a Guku:")
almacen.entregar_semillas(3)

print("Entregar a Yajirobe:")
almacen.entregar_semillas(9)

print("Cantidad de semillas disponibles:", almacen.get_cantidad())


print