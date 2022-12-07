class Clase1:
    def __init__(self):
        print('clase1.__init__')

    def metodo(self):
        print('Metodo clase1')

class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')
        super().__init__()
    def metodo(self):
        print('metodo clase2')
        super().metodo()
class Clase3(Clase1):
    def __init__(self):
        print('clase3.__init__')
        super().__init__()
    def metodo(self):
        print('metodo clase3')
        super().metodo()
class Clase4(Clase2,Clase3):
    
    def metodo(self):
        print('metodo clase4')
        super().metodo()

#
clase4 = Clase4()
#__bases__
print(Clase4.__bases__)
#mro
print(Clase4.__mro__)
#Cual metodo se ejecuta

clase4.metodo()