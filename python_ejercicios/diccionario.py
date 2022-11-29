#Profundizar en diccionarios 

#los dic guardan un orden (a diferencia de un set)
diccionario={'nombre':'Juan','apellido':'Perez','edad':28}
print(diccionario)

#los diccionarios son mutales pero las llaves deben de ser inmutables 
#diccionario= {[1,2]:'valor1'}
#diccionario={(1,2):'valor'}
print(diccionario)
#S agrega una llave con su valor si no se encuentra 
diccionario['departamento']='sistemas'
print(diccionario)
#No hay valores duplicados en las llave de un diccionario (si ya existe se remplaza )
diccionario['Nombres']='Juan carlos'
print(diccionario)

#recuperar un valor indicando una llave 
print(diccionario['Nombres'])
#Si no se encuentra la llave lanza una excepcion 
#print(diccionario['Nombres'])

#metodo get recupera una llave y si no existe lanza una excepcion 

print(diccionario.get('nombres','NO se encontro la llave'))
print(diccionario)

#setdefault i modifica si no encuentra el valor ,ademas se agrega un valor default

nombre=diccionario.setdefault('Nombrest','valor por default')
print(nombre)
print(diccionario)

#imprimir con pprint

from pprint import pprint as pp
#help(pp)
pp(diccionario, sort_dicts=False)