#alcance de variables (scape)

var_global = 'Variable global'

def imprimir():
    #acceder a una variable global 
    global var_global
    print(f'variable global de una funcion: {var_global}')

    #definicion de variable local
    var_local ='Variable local'
    print(f'variable local desde funcion : {var_local}')
    var_global='Nuevo valor variable global'
    
    def funcion_anidada():
        print(f'variable local dentro de la funcion anidada {var_local}')

    funcion_anidada()


imprimir()
print(f'variable global fuera de la funcion:{var_global}')

