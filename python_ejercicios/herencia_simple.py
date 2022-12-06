#ejemplo de herencia simplec
class ListaSimple:
    def __init__(self,elementos):
        self._elementos = list(elementos)

    def agregar(self,elemento):
        self._elementos.append(elemento)

    def __getitem__(self,indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos})'


class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        #ordenamos los elelmentos una vez inicializadas
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        #Ordenar el nuevo elemento
        self.ordenar()

class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        #una vez validados los elementos, los agregamos 
        super().__init__(elementos)

    def _validar(self,elemento):
        #validamos si el elemnto es de tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero: {elemento}')

        #sobrescibimos el emtodo agregar de la clase padre

    def agregar(self, elemento):
        self._validar(elemento)
        #una ves validado la agregamos a la lista
        super().agregar(elemento)


#lista simple
lista_simple = ListaSimple([5,3,6,8])
print(lista_simple)
#lista ordenada
Lista_ordenada = ListaOrdenada([4,3,6,9,10,-1])
print(Lista_ordenada)
Lista_ordenada.agregar(-14)
print(Lista_ordenada)
print(len(Lista_ordenada))
#lista enteros 
lista_enteros = ListaEnteros([1,3,4,-15])
print(lista_enteros)