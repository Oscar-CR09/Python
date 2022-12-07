#decoradores de clases
#permiten transformar de manera programatica nuestra clase 
#es similar a los decoradores de funciones (es metaprogramacion )
def decorador_repr(cls):
    print('1. Se ejecuta decorador ')
    print(f'recibimos el objeto de la clase: {cls.__name__}')
    #revisamos los atributos de la clase con el metodo vars
    atributos = vars(cls)
    #iteramos cada atributos
    #for nombre, atributo in atributos.items():
    #   print(nombre, atributo)
    #revisamos si se ha sobreescrito el metodo __init__ 
    import inspect

    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobrescito el metodo __init__')

    firma_init = inspect.signature(cls.__init__)
    print(f'Firma metodo __init__: {firma_init} ')
    #recuperamos los parametros excepto el primero que es self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'parametros init: {parametros_init}')
    #si por cada parametro tiene un metodo property asociado
    for parametro in parametros_init:
        #property es un valor de tipo buitl in para preguntar si 
        #se esta utilizando el decorador property

        es_metodo_property = isinstance(atributos.get(parametro), property)    
        if not es_metodo_property:
            raise TypeError(f'No existe un metodo property para el parametro: {parametro}') 

    #crer el metodo repr dinamicamente
    def metodo_repr(self):
        return f'resultado de ejecutar metodo repr '

    #agregar dinamicamente el metodo repr a nuestra clase
    setattr(cls, '__repr__', metodo_repr)

    return  cls
   

@decorador_repr
class Persona :
    def __init__(self, nombre, apellido):
        print('2. Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

#    def __repr__(self):
#        return f'Persona({self.nombre}, {self._apellido} )'


persona1 = Persona('juan', 'perez')
print(persona1)