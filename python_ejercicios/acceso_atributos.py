#Ejemplos atributos publicos, protegidos, privados 

class MiClase:
    def __init__(self,publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado


objeto = MiClase('valor publico', 'valor protegido', 'valor privado')
#acceso al atributo publico
print(objeto.publico)
#modificar el valor ppublco
objeto.publico = 'nuevo valor publico'
print(objeto.publico)

#acceso  del valor protegido
#solo dentro de la misma clase a clases hijas 
print(objeto._protegido)
#modificar atributos protegidos

objeto._protegido = 'Nuevo valor protegido'
print(objeto._protegido)

#acceder al valor privado
#print(objeto.__privado)
#pero , convierte . objeto._clase__atributo_privado
print(objeto._MiClase__privado)

#modificarvalor privado
objeto._MiClase__privado = 'Nuevo valor privado'
print(objeto._MiClase__privado)
