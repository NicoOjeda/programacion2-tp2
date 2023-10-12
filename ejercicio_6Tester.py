# 6. Construya un programa, utilizando la clase proveedora MonstersInc que, a partir de la entrada del usuario permita:
# a. Llamar a los métodos agregarMonstruo y agregarHumano.
# b. Filtrar a los monstruos con un nivel de energía específico por debajo de algún valor.
# c. Filtrar a los humanos por sus dos posibles estados: asustado y no asustado.

from ejercicio_4 import Monstruo
from ejercicio_2 import Humano
from ejercicio_5 import MonsterInc

class MonstersTester:
    
    def main(self):
        sullivan = Monstruo("James P. Sullivan", "leon")
        mike = Monstruo("Mike Wazowski", "ciclope")
        boo = Humano("Boo")
        pepe = Humano("pepe")
        monsterInc = MonsterInc()
        monsterInc.agregarMonstruo(mike)
        monsterInc.agregarMonstruo(sullivan)
        monsterInc.agregarHumano(boo)
        monsterInc.agregarHumano(pepe)
        sullivan.asustar(boo)
        
        print("1- Agregar Monstruo")
        print("2- Agregar Humano")
        print("3- Filtrar monstruo por nivel de energia menor a: ")
        print("4- Filtrar por humano asustado o no asustado")
        print('0- Salir')
        elegir = int(input("Elegi una opcion: "))
        while elegir !=0:
            if elegir == 1:
                # 6.a.
                nombre = str(input('elegir nombre: ' ))
                especie = str(input('elegir especie: ' ))
                nombre = Monstruo(nombre,especie)
                monsterInc.agregarMonstruo(nombre)
                print("Los monstruos son: "+ str(monsterInc.obtenerMonstruos()))
                print('===============================')
                print('===============================')
            elif elegir == 2:
                nombre = str(input('elegir nombre: ' ))
                nombre = Humano(nombre)
                monsterInc.agregarHumano(nombre)
                print("Los humanos son: "+ str(monsterInc.obtenerHumanos()))
                print('===============================')
                print('===============================')
            elif elegir == 3:
                # 6.B.
                nivel = int(input('-Filtrar monstruo con nivel menor a (escribir numero): '))
                for monstruo in monsterInc.obtenerMonstruos():
                    if monstruo.obtenerEnergia() < nivel:
                        print(str(monstruo) + " tiene menos de 100 de energia")
                print('===============================')
                print('===============================')
            elif elegir == 4:
                # 6.c.
                asustado = str(input('-Si queres filtrar por asustado ingresa la palabra "si" y si queres filtrar por no asustado ingresa "no": '))
                if asustado == "si":
                    for humano in monsterInc.obtenerHumanos():
                        if humano.obtenerEstadoAsustado() == True:
                            print(humano.obtenerNombre() + " esta asustado")
                elif asustado == "no":
                    for humano in monsterInc.obtenerHumanos():
                        if humano.obtenerEstadoAsustado() == False:
                            print(humano.obtenerNombre() + " no esta asustado")
                print('===============================')
                print('===============================')
            print("Elija otra opcion: ")
            print("1- Agregar Monstruo")
            print("2- Agregar Humano")
            print("3- Filtrar monstruo por nivel de energia menor a: ")
            print("4- Filtrar por humano asustado o no asustado")
            print('0- Salir')
            elegir = int(input("Elegi una opcion: "))

        
        # print(monsterInc.obtenerMonstruos())
        # print(monsterInc.obtenerHumanos())
        # monsterInc.eliminarMonstruo(sullivan)
        # print(monsterInc.obtenerMonstruos())
        # monsterInc.eliminarHumano(boo)
        # print(monsterInc.obtenerHumanos())
        

if __name__ == "__main__":
    monstersTester = MonstersTester()
    monstersTester.main()