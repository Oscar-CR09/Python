#Exprecion generadora (es un generador anonimo )

multiplicacion = (valor*valor for valor in range(4))

print(multiplicacion)
print(type(multiplicacion))

print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

# tambien se puede pasar una exprecion generadora a una funcion (sin parantesis)

import math

suma = sum(valor*valor for valor in range(4))
print(f'resultado suma: {suma}')

#tambien se puede usar una lista o cualquier otro iterador 

lista = ['juan','perez']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

# crear un string apartir de un generador creado apartir de una lista 
lista = ['karla','gomez',22]
contador = 0
#definimos una funcion para incremetar el contador 
def incrementar():
    global contador 
    contador +=1 
    return contador

#la primera para es el yield, la segunda es el for, entre parentesis 

generador = (f'{incrementar()}.{nombre}' for nombre in lista)
lista = list(generador)

print(lista)

cadena = ', '.join(lista)
print(f'cadena generada {lista}')