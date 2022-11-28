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