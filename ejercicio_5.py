from ejercicio_4 import Monstruo
from ejercicio_2 import Humano


class MonsterInc:
    
    def __init__(self):
        
        self.monstruos = []
        self.humanos = []
        
    def agregarMonstruo(self, mon: Monstruo):
        self.monstruos.append(mon)
    
    def agregarHumano(self, hum: Humano):
        self.humanos.append(hum)
        
    def obtenerMonstruos(self):
        return self.monstruos
    
    def obtenerHumanos(self):
        return self.humanos
    
    def eliminarMonstruo(self, monstruo: Monstruo):
        self.monstruos.remove(monstruo)
    
    def eliminarHumano(self, humano: Humano):
        self.humanos.remove(humano)
    
    def imprimir(self):
        print("================================================")
        print("Los elementos humanos son:  " [str(id(self.humanos))])
        # print("agumon1 [" + str(id(agumon1)) + "] == tentomon1 [" + str(id(tentomon1)) + "]: " + str(agumon1 == tentomon1))



sullivan = Monstruo("James P. Sullivan", "leon")
mike = Monstruo("Mike Wazowski", "ciclope")
boo = Humano("Boo")

monsterInc = MonsterInc()
monsterInc.agregarMonstruo(mike)
# print(monsterInc.obtenerMonstruos())
