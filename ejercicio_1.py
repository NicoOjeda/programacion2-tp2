# 1. Dado el siguiente diagrama de clases:
#     Genere la clase Monstruo, conteniendo los atributos y servicios mencionados en el diagrama de clases anterior.
# a. El atributo de clase maxEnergía debe tener un valor de 100.
# b. El valor inicial de energia debe ser igual a maxEnergía.
# c. El método asustar debe decrementar la energía del monstruo en 10 unidades.

class Monstruo:
    
    maxEnergia= 100
    
    def __init__(self, nom: str, esp: str):
        self.nombre = nom
        self.especie = esp
        self.energia = Monstruo.maxEnergia
    
    def establecerNombre(self,nom:str):
        self.nombre = nom
            
    def obtenerNombre(self):
        return self.nombre
    
    def establecerEspecie(self,esp: int):
        self.especie = esp
            
    def obtenerEspecie(self):
        return self.nombre
    
    def establecerEnergia(self,ene: int):
        self.energia = ene
    
    def obtenerEnergia(self):
        return self.energia
    
    def asustar(self):
        self.energia -= 10
        
    def imprimir(self):
        print(self.nombre + " " + self.especie +" "+ str(self.energia))
        
    def __repr__(self):
        return self.nombre
        
# monstruo1 = Monstruo("pepe", "reptil")
# monstruo2 = Monstruo("luis", "ave")

# monstruo1.imprimir()
# monstruo2.imprimir()
# Monstruo.asustar(monstruo1)
# print(Monstruo.obtenerEnergia(monstruo1))
# monstruo1.establecerNombre("mario")
# monstruo1.imprimir()
