#help(str(partition))

hora, _, minutos = '17:20'.partition(':')
#print(type(variable))
print(hora, minutos)

#listas son mutables

nombres1 = ['Juan','karla','Pedro']
nombres2 = 'Laura Maria gonzalo ernesto'.split()
#suma listas 
print(f'Sumar listas {nombres1 +nombres2}')
#extender una lista con otra lista 
nombres1.extend(nombres2)
print(f'externder la lista1 y la listas:  {nombres1}')

#lista de numeros
numeros1=[10,40,15,4,20,90,4]
print(f'original: {numeros1}')

#obtener el indice del primer elemento encontrado de la lista 
#help(list.index)
print(f'indice 4: {numeros1.index(4)}')
#invertir el orden de los elementos 
numeros1.reverse()
print(f'Lista invertida: {numeros1}')
#ordener los elementos de una lista asendente 
numeros1.sort()
print(f'lista ordenada: {numeros1}')
numeros1.sort(reverse=True)
print(f'Lista ordenada desendente: {numeros1} ')
#obtener el numero minimo o maximo de una lista 
print(f'valor minimo: {min(numeros1)}')
print(f'valor maximo: {max(numeros1)}')
numeros5 = numeros1.copy()
print(numeros1)
print(numeros5)
print(f'misma referencia netre las lista: {nombres1 is numeros5 }')
print(f'mismo contenido: {numeros1 == numeros5}')
numeros5  = list(numeros1)
print(f'misma referencia netre las lista: {nombres1 is numeros5 }')
print(f'mismo contenido: {numeros1 == numeros5}')

numeros5 = numeros1[:]
print(f'misma referencia netre las lista: {nombres1 is numeros5 }')
print(f'mismo contenido: {numeros1 == numeros5}')

#multiplicacion de listas 
lsita_multiplicacion = 5*[[2,5]]
print(lsita_multiplicacion)
print(f'misma referencia: {lsita_multiplicacion[0] is lsita_multiplicacion[1]}')
print(f'misma contenido: {lsita_multiplicacion[0] == lsita_multiplicacion[1]}')
lsita_multiplicacion[2].append(10)
print(lsita_multiplicacion)

#matrises en python 
matriz = [[10,20,],[30,40,50],[60,70,80,90]]
print(f'matriz original: {matriz}')
print(f'renglon 0, columna 0 : {matriz[0][0]}')
print(f'renglon 2, columna 2: {matriz[2][2]}')
matriz[2][0]=65
print(f'matriz modificada: {matriz}')

lista_listas = [[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,61,70]] 
lista_listas.sort(key=len)
print(f'Ordenar lista: {lista_listas}')

# sorted built-in
#help(sorted)

nombres1=['Juan carlos ', 'Karla','Pedro','Esperanza']
nombres1 = sorted(nombres1)
print(nombres1)
#ordenar de modo desendente 
nombres1 = sorted(nombres1,reverse=True)
print(nombres1)
#ordenar por la cantidad de caracter largo
nombres1 = sorted(nombres1, key=len)
print(nombres1)
#built-in reversed
nombres1 = reversed(nombres1)
print(list(nombres1))