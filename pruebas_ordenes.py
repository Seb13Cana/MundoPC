from MundoPC.computadora import Computadora
from monitor import Monitor
from orden import Orden
from raton import Raton
from teclado import Teclado

#Se crea elementos de cada computadora
#Computadora 1
raton_1 = Raton('Asus', 'Tipo C')
teclado_1 = Teclado('HP','USB')
monitor_1 = Monitor('HP','25"')
computadora_1 = Computadora('HP Desktop',monitor_1,teclado_1,raton_1)
#Computadora_2
raton_2 = Raton('Nexus','Bluetooh')
teclado_2 = Teclado('Nexus', 'USB')
monitor_2 = Monitor('Nexus', 37)
computadora_2 = Computadora('Nexus PC',monitor_2,teclado_2,raton_2)



ordenes_computadora = [computadora_1,computadora_2]
orden_1 = Orden(ordenes_computadora)

#Computasor 3
monitor_3 = Monitor('Apple', 35)
raton_3 = Raton('Apple','USB')
teclado_3 = Teclado('Apple', 'USB')
computadora_3 = Computadora('Apple PC',monitor_3,teclado_3,raton_3)
print(orden_1)

orden_1.agregar_computadora(computadora_3)
print(orden_1)
