#simulacion de sobrecarga de contructores en python 
#otras formas de crear objetos

class Persona:
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)

    @classmethod
    def crear_persona_con_valores(cls,nombre,apellido):
        return cls(nombre, apellido)


    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'

persona1 =Persona('Juan', 'Perez')

persona_vacia = Persona('Juan', 'Perez')
print(persona1)
persona_vacia = Persona.crear_persona_vacia()

print(persona_vacia)

crear_persona_con_valores = Persona.crear_persona_con_valores('Karla', 'Gomez')
print(crear_persona_con_valores)