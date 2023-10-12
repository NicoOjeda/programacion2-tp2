# 4. Modificar la clase Monstruo de acuerdo a lo especificado al siguiente diagrama:
# a. El comando asustar debe, además de decrementar la energía del monstruo en 10 unidades, cambiar el valor del atributo estadoAsustado de hum a True.
# b. El comando divertir debe decrementar la energía del monstruo en 20 unidades, cambiando el valor del atributo estadoAsustado de hum a False.

from ejercicio_2 import Humano

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
    
    
    def asustar(self, hum: Humano):
        self.energia -= 10
        hum.establecerEstadoAsustado(True)
    
    def divertir(self, hum: Humano):
        self.energia -= 20
        hum.establecerEstadoAsustado(False)
        
    def imprimir(self):
        print(self.nombre + " " + self.especie +" "+ str(self.energia))
        
    def __repr__(self):
        return self.nombre


# c. Una vez codificadas las modificaciones sobre la clase del punto anterior, ejecute el siguiente programa Python y verifique que se cumpla la salida esperada.

# sullivan = Monstruo("James P. Sullivan", "leon")
# mike = Monstruo("Mike Wazowski", "ciclope")
# boo = Humano("Boo")
# print(sullivan.obtenerEnergia())
# print(mike.obtenerEnergia())
# print(boo.obtenerEstadoAsustado())
# sullivan.asustar(boo)
# print(sullivan.obtenerEnergia())
# print(mike.obtenerEnergia())
# print(boo.obtenerEstadoAsustado())
# mike.divertir(boo)
# print(sullivan.obtenerEnergia())
# print(mike.obtenerEnergia())
# print(boo.obtenerEstadoAsustado())
