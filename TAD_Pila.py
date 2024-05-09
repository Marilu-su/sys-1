def crearPila():
    #crea una pila vacia
    pila = []
    return pila

def esVacia(pila):
    #retorna TRUE or FALSE si la pila esta o no vacia
    return len(pila) == 0

def apilar(pila, elem):
    #Agrega un elemento al final de la pila 
    pila.append(elem)

def desapilar(pila):
    #retorna Y ELIMINA el ultimo elemneto de la pila
    elem = pila[len(pila)-1]
    pila.pop() #saca el elemneto de la pila
    return elem

def tamanioPila(pila):
    #retorna la cantidad de elemnetos de la pila
    return len(pila)

def copiarPila(pila1, pila2):
    #copia los datos de una pila a otra
    aux = crearPila() #se crea porque se pierden los datos de una pila y no queremos eso
    while not esVacia(pila1):
        elem = desapilar(pila1)
        apilar(aux, elem)
    while not esVacia(aux):
        elem = desapilar(aux)
        apilar(pila1, elem)
        apilar(pila2, elem)