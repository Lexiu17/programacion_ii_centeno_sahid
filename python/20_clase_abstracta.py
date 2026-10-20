from abc import ABC, abstractmethod

class Nave_Espacial(ABC):
    modelo: str
    def __init__(self, modelo: str):
        self.modelo = modelo

    @abstractmethod
    def despegar(self):
        pass

class Nave_Capsula(Nave_Espacial):
    modelo: str
    def __init__(self, modelo: str):
        super().__init__(modelo)

    def despegar(self):
        print(self.modelo, "Despega con motores de Capsule Corp")

class Sayayin(Nave_Espacial):
    
    def __init__(self, modelo: str):
        super().__init__(modelo)

    def despegar(self):
        print(self.modelo, "Despega inmediatamente")

Nave_Bulma = Nave_Capsula("Nave de bulma")
Nave_Vegeta = Sayayin("Capsula Sayayin")
Nave_Bulma.despegar()
Nave_Vegeta.despegar()
