# Se agrega el siguiente diagrama, que intenta representar a los humanos del referenciado universo:
# Habiendo analizado el diagrama, genere la clase Humano con los atributos y servicios mencionados en dicho diagrama.
# a. El atributo de clase especie debe tener valor “humano”.
# b. El valor inicial de estadoAsustado debe ser False.    

class Humano:
    
    especie= "humano"
    
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.estadoAsustado = False
        self.especie = Humano.especie
        
    def establecerNombre(self, nom: str):
        self.nombre = nom
    
    def obtenerNombre(self):
        return self.nombre
    
    def establecerEstadoAsustado(self, est: bool):
        self.estadoAsustado = est
    
    def obtenerEstadoAsustado(self):
        return self.estadoAsustado
    
    def imprimir(self):
        print(self.nombre + " " + str(self.estadoAsustado) + " " + str(self.especie))
    
    def __repr__(self):
        return self.nombre
        

boo = Humano("Boo")
boo.establecerEstadoAsustado(True)
boo.imprimir()