numeros = range(10)
lista_pares = []

#creamos una lista con los valores pares 

for numero in numeros:
#revisar si es un numero par
    if numero % 2 == 0:
        lista_pares.append(numero*numero)


print(f'Lista pares: {lista_pares}')

#se hace con list comprehensions
#[exprecion for var in coleccion if condicion ]
##la condicion del if es opcional

lista_pares = []
lista_pares = [numero*numero for numero in numeros if numero % 2 ==0 ]
print(f'Lista pares con list comprehecion: {lista_pares}')

#un ejemplo similar con cos condiciones (las condiciones son opcionales 
# solo se agrega el valor a la lista cuando el valor cumple ambas condiciones 
#es decir, debe ser divicible entre 2 y divicible entre 6

pares = [numero for numero in range(50) if numero%2==0 if numero%6==0]
print(f'Lista divicible entre 2 y netre 6 {pares} ')
#agregando if else 
lista_pares = []
lista_impares = []
for numero in range(10):
    if numero%2==0:
        lista_pares.append(numero)

    else:
        lista_impares.append(numero)

print(f'Pares: {lista_pares}')
print(f'impares: {lista_impares}')

#el mismo ejercicio usando list comprehencio
lista_pares = []
lista_impares = []

[lista_pares.append(numero) if numero%2==0 else lista_impares.append(numero) for numero in range(10)]

print(f'Pares: {lista_pares}')
print(f'impares: {lista_impares}')
