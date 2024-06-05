class Orden:
    contador_orenes = 0

    def __init__(self, computadoras):
        Orden.contador_orenes += 1
        self.id_orden = Orden.contador_orenes
        #Recibimos lista de objetos Computadora
        self.computadoras = computadoras

    def agregar_computadora(self,computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self.computadoras:
            computadoras_str += '\n' + computadora.__str__()

        return f'''Orden: {self.id_orden}
    Computadoras: 
        {computadoras_str}'''