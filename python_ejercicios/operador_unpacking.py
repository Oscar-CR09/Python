numeros = [1,2,3]
print(numeros)
print(*numeros)
print(*numeros, sep=' - ')

#desempaquetando 
def suma(a,b,c):
    print(f'resultado de la suma: {a+b+c}')

suma(*numeros)
#extraer algunas partes de una lista
mi_lista=[1,2,3,4,5,6]
a,*b,c,d = mi_lista
print(a,b,c,d)

lista1=[1,2,3]
lista2=[4,5,6]
lista3=[lista1,lista2]
print(f'Lista de lista: {lista3}')
lista3=[*lista1,*lista2]
print(f'unir listas: {lista3}')
#unir diccionarios
dic1 ={'A':1,'b':2,'c':3}
dic2 = {'d':4,'e':5}
dic3 = {**dic1,**dic2}
print(f'unir diccionarios: {dic3}')
#contruir una lista a partir de un str
lista = [*'HolaMundo']
print(lista)
print(*lista,sep='')