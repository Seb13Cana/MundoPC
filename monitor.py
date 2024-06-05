
class Monitor:
    contador_monitor = 0

    #Constructor

    def __init__(self, marca, tamanio):
        Monitor.contador_monitor +=1
        self.id_monitor = Monitor.contador_monitor
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self):
        return (f'Id: {self.id_monitor}, Marca: {self.marca},'
                f'Tamaño: {self.tamanio}')


if __name__ == '__main__':
    monitor_1 = Monitor('HP','25"')

    print(monitor_1)