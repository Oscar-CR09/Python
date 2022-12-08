from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True,frozen=True)
class Domicilio:
    calle:str
    numero: int =0 

@dataclass (eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str 
    domicilio: Domicilio
    contador_persona: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor nombre vacio: {self.nombre}')

domicilio1 = Domicilio('Saturno', 15)
persona1 = Persona('Juan', 'Perez', domicilio1)
print(f'{persona1!r}')
#Variable de clase
print(f'Variable clase: {Persona.contador_persona}')
#variables de instancias 
print(f'Variables de instancias {persona1.__dict__}')
#variable con valores vacios
persona_vacia = Persona('Karla', '',None)
print(f'Persona vacía:{persona_vacia }')
#revisar igualdad entre objetos (__eq__)
persona2 = Persona('Juan', 'Perez',Domicilio('Jupiter',30))
print(f'Objetos iguales?: {persona1 == persona2}')
#agregar esta clase a una coleccion
coleccion = {persona1,persona2}
print(coleccion)
#frozwn =true 
