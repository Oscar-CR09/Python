#funcion lambda 
#son funciones anonimas y son pequeñas (una linea de codigo)

#no es posible asignar una funcion a una variable 

#def sumar(a,b):
#    return a+b

    #la funcion lamnda (anonima, sin nombre, y una sola linea de codigo)
    #No se necesita agregar parantesis para los parametros
    #No se necesita usar la palabra reservada return, pero si debe regresar una expreción

mi_funcion_lambda = lambda a,b: a + b 

resultado = mi_funcion_lambda( 4,6 )
print(f'resultado de sumar con funcion lambda: {resultado}')

#Funcion lambda que no recibe argumentos (debe regresar una exprecion valida)
mi_funcion_lambda = lambda:'Funcion sin argumentos'

print(f'llamar funcion lambda sin argumentos: {mi_funcion_lambda()} ')

#funcion lambda con parametros por default
mi_funcion_lambda = lambda a=2 , b=3 : a + b

print(f' Funcion con parametros por default: {mi_funcion_lambda(4,6)}')

#funciones lambda con argumentos variables *arg y **kwargs

mi_funcion_lambda = lambda * args, **kwargs: len(args) + len(kwargs)
print(f'resultado de argumentos variables: {mi_funcion_lambda(1,2,3, a=5, b=6)}')

#funciones lambda con arguemntos, argumentos variables y valores por defaul

mi_funcion_lambda = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)

print(f'resultado funcion lambda: {mi_funcion_lambda(1,2,4, 5,6,7, e=5,f=7)}')