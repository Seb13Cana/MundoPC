from monitor import  Monitor
from raton import Raton
from teclado import  Teclado
class Computadora:
    contador_computadora = 0

    def __init__(self, nombre, monitor,teclado, raton):
        Computadora.contador_computadora +=1
        self.id_computadora = Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.teclado= teclado
        self.raton = raton


    def __str__(self):
        return f'''\n{self.nombre}:  {self.id_computadora}
    Monitor: {self.monitor}
    Teclado: {self.teclado}
    Raton: {self.raton}'''

#CDodigo principal
#Se crea primero los especificos porque cada parte es una pieza de la compiutadora
#Se debe agregar la condición if nname == main

if __name__ == '__main__':
    monitor_1 = Monitor('HP',32)
    teclado_1 = Teclado('HP', 'Tipo C')
    raton_1 = Raton('HP', 'USB')
    computadora_1 = Computadora('HP Desktop',monitor_1,teclado_1,raton_1)

    print(computadora_1)
