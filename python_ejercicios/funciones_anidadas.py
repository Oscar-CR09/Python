#Funciones anidadas

def calculadora(a, b, operacion='sumar'):
    #1 definir funcion anidada
    def sumar(a, b):
        return a + b

    def restar(a,b):
        return a-b

        #2. llamamos a la funcion anidada
    if operacion == 'sumar':
        print(f'resultado sumar: {sumar(a,b)}')
    elif operacion == 'restar':    
        print(f'resultado resta: {restar(a, b)}')

calculadora(5, 6)
calculadora(10, 2, operacion='restar')
