#Profundizar en set
#Un set es una coleccion de elementos unicos y es mutable
#Los elementos de un set debe ser inmutables 

#conjunto = {[1,2]},{[3,4]}
conjunto = {'Juan',True, 18.0}
print(conjunto)
print(type(conjunto))
#conjunto = {} gernera un dic vacio
#print(type(conjunto))
#set vacio correcto

conjunto = set()

print(conjunto)

print(type(conjunto))
conjunto.add('Juan')
print(conjunto)
#crear un set a partie de una iterable
conjunto = set ([4,5,7,8,4 ])
print(conjunto)
#podemos agregar mas elementos incluso un set mas
conjunto2 = {100,200,300,300}
conjunto.update(conjunto2)
print(conjunto)

conjunto.update([20,30,40,40])
print(conjunto)
 
 #compiar un set (copia poco profundas solo copia referencia)

conjunto_copia= conjunto.copy()
print(conjunto_copia)
#verificar la igualdad delos sets
print(f'es igual en contenido: {conjunto == conjunto_copia} ')

print(f'es la misma referencia {conjunto is conjunto_copia} ')

#operaciones de conjuntos con sets
#Personas con distinas caracteristicas

pelo_negro = {'Juan','karla', 'pedro','maria'}
pelo_rubio = {'Lorenzo','Laura','marco'}
ojos_cafes = {'Karla','Laura'}
menores_30 = {'juan','karla','maria'}

#Todos con ojos_cafes y pelo rubio (union)(no se repite los elementos)
print(ojos_cafes.union(pelo_rubio))

#invertir el orden con el mismo resultado 
print(pelo_rubio.union(ojos_cafes))

#interseccion intersection solo
print(ojos_cafes.intersection(pelo_rubio))
#difference (no es conmutable)
#las personas que se encuentran en el primer set pero no es el segundo 
print(pelo_negro.difference(ojos_cafes))

#diferencia simetrica
#no ambas (conmutativas)
print(pelo_negro.symmetric_difference(ojos_cafes))

#preguntar es un set esta contenido en otro(subset)
#revisar si los elementos del primer set estan contenidos en el segundo set 

print(menores_30.issubset(pelo_negro))
#si un set coontiene otro set superset

print(menores_30.issuperset(pelo_negro))

#(distjoint)
print(pelo_negro.isdisjoint(pelo_rubio))