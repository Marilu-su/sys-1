# misma explicacion que TAD_Pila
"""
#def crearCola():
    Crea una cola vacia

#def esVacia(cola):
    Retorna Verdadero si la cola no tien elementos

#def encolar(cola, elem):
    Agregar un elemneto al final de la cola

#def desencolar(cola, elem):
    Retorna y elimina el primer elemento de la cola

#def tamanio(cola):
    Retorna la cantidad de elementos de la cola

#def copiarCola(cola1, cola2)
    Copia los datod de una cola a otra

    
    ------Estructura Interna:
cola = []
cola = [""]

"""
def crearCola():
    cola = []
    return cola

def esVacia(cola):
    return len(cola) == 0

def encolar(cola, elem):
    cola.append(elem)

def desencolar(cola):
    elem = cola[0]
    del cola[0]
    return elem

def tamanioCola(cola):
    return len(cola)

def copiarCola(cola1, cola2):
    #copia los datos de una pila a otra
    aux = crearCola() #se crea porque se pierden los datos de una pila y no queremos eso
    while not esVacia(cola2):
        elem = desencolar(cola2)
        encolar(aux, elem)
    while not esVacia(aux):
        elem = desencolar(aux)
        encolar(cola1, elem)
        encolar(cola2, elem)