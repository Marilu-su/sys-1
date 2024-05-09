# En una empresa de logística, se gestiona el movimiento de camiones que transportan mercancías entre diferentes puntos de distribución. Cada camión tiene asignada una
# placa, y al ingresar al centro logístico se registra la hora de entrada y el punto de origen o destino al que se dirige. Al salir del centro, se registra la hora de salida y se calcula el tiempo de permanencia.

# Se deberá desarrollar una aplicación utilizando las estructuras de datos necesarias. 

# Se desea tener un menú con las siguientes opciones:

# 1. Registrar ingreso, modificar información y eliminar camión: Permite registrar la entrada de un nuevo camión, modificar su información o eliminarlo del registro, utilizando su placa como referencia.

# 2. Registrar salida de camión: Registra la salida de un camión del centro logístico, calculando el tiempo de permanencia y generando un informe de la estadía.

# 3. Listado de camiones: Muestra un listado completo de todos los camiones que están dentro del centro logístico, incluyendo su placa, hora de entrada y punto de origen/destino.

# 4. Informe de movimientos por punto de distribución: Genera un informe que indica la cantidad de camiones que han llegado o salido de cada punto de distribución durante un período determinado.

# 5. Camiones en horario de mayor actividad: Muestra los camiones que han ingresado al centro logístico durante el horario de mayor actividad, que comprende desde las 8:00 hasta las 12:00 y desde las 14:00 hasta las 18:00.

# 6. Eliminar camiones que ingresaron después de cierto horario: Permite eliminar los registros de camiones que han ingresado al centro logístico después de un horario específico, liberando espacio en la base de datos.

# 7. Generar una cola de camiones por punto de distribución: Crea una cola con los camiones que están esperando para ingresar o salir de un punto de distribución específico, facilitando la organización del flujo de vehículos.


# Importacion de TADS

from TAD_Empresa import*
from TAD_Camion import*
from TAD_Pila import*
from TAD_Cola import*

#Definicion de funciones

def menu(op):
    # menu interactivo
    if(op == 1):
        RegistarIngresoCamiones()
    elif(op == 2):
        modificarInformacion()
    elif(op == 3):
        eliminarCamion()
    elif(op == 4):
        registrarSalida()
    
    #elif(op == 4): 
    #   cambiarNota()
    #elif(op == 5):
    #   coloquioTeorico()
    # elif(op == 6):ñ
    #   correcionExamenP()
    # elif(op == 7):
    #    calcularProm()
    else:
        print("termino las opciones")
        op = 'no'

def RegistarIngresoCamiones():
    # placa, horaE, minE, origen, horaS, minS
    seg = input("Quiere ingresar un camion? (s/n)")
    seg.lower()
    while seg != 'n':
        camion = crearCamion()
        placa = input("ingrese la patente del camion: ")
        fechaE = input("ingrese la fecha de entrada del camion: ")
        horaE = int(input("ingrese el horario de entrada del camion (sin los minutos): "))
        minE = int(input("ingrese el minuto de entrada del camion: "))
        origen = input("ingrese el origen del camion: ")
        fechaS = '00/00/0000'
        horaS = 0
        minS = 0
        cargarCamion(camion, placa, fechaE, horaE, minE, origen, fechaS, horaS, minS)
        agregarCamion(empresa, camion)
        seg = input("Quiere ingresar otro camion? (s/n)")
        seg.lower()

def buscarCamionPorPatente(patente):
    # busca al estudiante por legajo y lo retorna
    tam = tamanio(empresa)
    for i in range (1, tam+1):
        camion = recuperarCamion(empresa, i)
        if (verPlaca(camion) == patente):
            return camion
            break

def modificarInformacion():
    patente = input("Ingrese la patente del camión a modificar: ")
    camion = buscarCamionPorPatente(patente)
    modificar_camion = True
    modificar_informacion = True

    while modificar_camion:
        while modificar_informacion: 
            aux = input("¿Qué quiere modificar?: (placa, fechaE, horaE, minE, origen, fechaS, horaS, minS)")
            if (aux == "patente"):
                nuevo = input("Ingrese la nueva placa: ")
                modPlaca(camion, nuevo)
            elif (aux == "fechaE"):
                nuevo = input("Ingrese la nueva fecha de entrada: ")
                modFechaEntrada(camion, nuevo)
            elif (aux == "horaE"):
                nuevo = int(input("Ingrese la nueva hora de entrada: "))
                modHoraEntrada(camion, nuevo)
            elif (aux == "minE"):
                nuevo = int(input("Ingrese los nuevos minutos de entrada: "))
                modMinEntrada(camion, nuevo)
            elif (aux == "origen"):
                nuevo = input("Ingrese el nuevo origen/destino del camion: ")
                modOrigen(camion, nuevo)
            elif (aux == "fechaS"):
            nuevo = input("Ingrese la nueva fecha de salida: ")
            modFechaSalida(camion, nuevo)
        elif (aux == "horaS"):
            nuevo = int(input("Ingrese la nueva hora de salida: "))
            modHoraSalida(camion, nuevo)
        elif (aux == "minS"):
            nuevo = int(input("Ingrese los nuevos minutos de salida: "))
            modMinSalida(camion, nuevo)
        

        modificar_informacion = input("Si hay más informacion para modificar del mismo camion: ingrese True. Si no, ingrese False")
    

def eliminarCamion():
    op = 's'
    while op != 'n':
        pat = input("ingrese la patente del camion que desea eliminar: ") 
        camion = buscarCamionPorPatente(pat)
        eliminarCamion(empresa, camion)
        print(f"Camion con patente {pat} se elimino")
        op = input("quiere eliminar otro camion: (s/n)")
        op.lower()

def registrarSalida():
    patente = input("Ingrese patente del camion")
    
#Codigo Principal
    
empresa = crearEmpresa()

seg = input("Quiere hacer alguna accion con algun estudiante?: (si, no) \n")
seg.lower()

while seg != 'no':  
    print("Elija la opcion que quiera hacer")
    print("1. Registrar ingreso de un camion")
    print("2. Modificar información de un camion")
    print("3. Eliminar camion")
    print("4. Registrar salida del camion")
    print("5. ")
    print("6. ")
    print("7. ")
    print("8. salir")
    op = int(input("opcion:  ")) #op es la Opcion que se eliga
    menu(op)
    seg = input("Quiere hacer alguna accion con algun estudiante?: (si, no) \n")
    seg.lower()