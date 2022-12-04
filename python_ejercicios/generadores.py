#Generadores
#Es una funcion especial en python , retorna una secuencia de valores
#suspende la eejcucion de la funcion yield (producir) (no se usa return)

def genereador():
    yield 1
    print('se reanuda la ejecucion ')
    yield 2
    print('se reanuda la ejecucion ')
    yield 3

#consume el generador a demanda 

gen = genereador()

# con cada llamada cosumimos un valor 
print(next(gen))

print(next(gen))

print(next(gen))
# si se trata consumir mas valores de los que produce el generador 
#lanza un error de stopiteration

#consumiendo los valores del generador con ciclo for 

for valor in genereador():
    print(f'Numero generador: {valor}')