class Persona:
    contador_personas = 0

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

#monstrar los atributos de un objeto
persona1 = Persona('Juan', 'Perez')
print(persona1.__dict__)

#crear un atributo al vuelo
print(persona1.contador_personas)#accediendo al atributo de clase
#pero no es posible modifiar con el objeto, si no con la clase
persona1.contador_personas = 10
print(persona1.__dict__)
#atributo anterior oculta el atributo de clase 
print(Persona.contador_personas)
print(persona1.contador_personas)

#un segundo objeto 
persona2 = Persona('karla', 'Gomez')  
print(persona2.__dict__)
print(persona2.contador_personas)
#asociar un atributo de clase al vuelo 

Persona.contador2 = 20
print(Persona.contador2)