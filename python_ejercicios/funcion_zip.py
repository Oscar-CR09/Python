#print(dir(__builtins__))
#help(zip)

numeros=[1,2,3]
letras=['a','b','c','d']
identificador=321,322,323,324,325
conjunto={6,4,0,9,8,15,10}
mezcla= zip(numeros,letras,identificador,conjunto)
#print(mezcla)
print(list(mezcla))
#print(tuple(zip(numeros,letras)))
#print(type(mezcla))
#iterar en paralelo
for numero, letra,id,aleatorio in zip(numeros,letras,identificador,conjunto):
    print(f'NUmero: {numero},letra: {letra}, id: {id}, aleratorio: {aleatorio}')

nuevalista = []
for numero, letra, id, aleatorio in zip(numeros, letras, identificador, conjunto):
     nuevalista.append(f'{id}-{numero}-{letra}-{aleatorio}')
print(nuevalista)    

#unzip

mezcla = [(1,'a'),(2,'b'),(3,'c')]
numeros,letras =zip(*mezcla)
print(f'Numeros: {numeros}, letras: {letras}')

#ordenamientousando zip
letras = ['c','d','a','e','b']
numeros = [3,2,1,4,5]
mezcla = zip(letras,numeros)
#sin ordenar
print(tuple(mezcla))
#ordenar
print(sorted(zip(letras,numeros)))
#crear un diccionario con zip y dos iterables

llaves = ['Nombre','apellido', 'edad']
valores = ['juan','perez',18]
diccionario = dict(zip(llaves,valores))
print(diccionario)

#actualizar un elemento de diccioanrio
llave = ['edad']
nueva_edad = [28]
diccionario.update(zip(llave, nueva_edad))
print(diccionario)
