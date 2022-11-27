#profundizando en tuplas

#declaracion de variables
a,b = 'hola', 'adios'
print(a,b)
#swap (intercambio)
a,b = b,a
print(a,b)

#regresar multiples valores en una funcion 

def minmax(elementos):
    return min(elementos),max(elementos)


min, max = minmax([1,2,3,4,5])

print(f'valor min: {min}, valor max: {max}')
#regresa la suma de uan tupla

resultado = sum((1,2,3,4,5))

print(f'resultado: {resultado}')

def sumar(*args):
    return sum(args)

resultado=sumar(1,2,3,4,5)
print(f'resultado: {resultado}')
