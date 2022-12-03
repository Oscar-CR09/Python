#las funciones en python son ciudadanas de primera clase
#first class citizens
#definimos la funcion 

def sumar(a,b):
    return a+b

#asignar una funcion a una varables (no se usa parantesis)

mi_funcion = sumar
#verificar el tipo de variable

print(type(mi_funcion))

#llamamamos la funcion atravez de la variable 

resultado = mi_funcion(5,8)
print(f'resulatado: {resultado} ')

#2. funcion como argumento

def operacion(a,b,sumar_arg):
    print(f'resultado sumar: {sumar_arg(a,b)}')

operacion(4, 5, sumar)  
# 3. retornar una funcion

def retornar_funcion():
    #retornamos la funcion
    return sumar

mi_funcion_retornada = retornar_funcion()
print(f'resultado funcion retornada {mi_funcion_retornada(5,7)}')