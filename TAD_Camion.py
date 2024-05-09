"""
------Especificación:

    • Nombre del TAD: TAD Camion (archivo TAD_Camion.py)
    • Sirve para almacenar los datos de camiones con placa, hora de Entrada, minutos de Entrada, origen/destino, hora de salida, minutos de salida 
    • Operaciones Básicas:

#def crearCamion()
    Crea una camion Nuevo
    
#def cargarCamion(camion, placa, horaE, minE, origen, horaS, minS)
    Carga los datos al camion que se le pase, indicando placa, hora de entrada, minuto de dentrada, origen o destino, hora de salida, minutos de salida

#def verPlaca(camion)
    Devuelve la placa del camion
#def verHoraEntrada(camion)
    Devuelve la hora de entrada del camion
#def verMinEntrada(camion)
    Devuelve los minutos de entrada del camion
#def verOrigen(camion)
    Devuelve el origen o destino del camion
#def verHoraSalida(camion)
    Devuelve hora de salida del camion
#def verMinSalida(camion)
    Devuelve minutos de salida del camion
    
#def modPlaca(camion, placaN)
    Modifica la placa del camion , pasandole una nueva 
#def modHoraEntrada(camion, horaEN)
    Modifica la hora de entrada del camion , pasandole una nueva 
#def modMinEntrada(camion, minEN)
    Modifica los minutos de entrada del camion , pasandole una nueva 
#def modOrigen(camion, origenN)
    Modifica origen o destino del camion , pasandole una nueva 
#def modHoraSalida(camion, horaSN)
    Modifica hora de salida del camion , pasandole una nueva 
#def modMinSalida(camion, minSN)
    Modifica la minutos de salida del camion , pasandole una nueva 
#def copiar(camion1, camion2)
    Copia todos los datos del primer camion que se le pase, al segundo


------Estructura Interna: 
camion = [placa, horaE, minE, origen, horaS, minS]
camion = ["",0,0,"", 0,0]

"""
def crearCamion(): 
    camion = ["", 0, 0, "", 0, 0]
    return camion

def cargarCamion(camion, placa, fechaE, horaE, minE, origen, fechaS, horaS, minS):
    camion[0] = placa
    camion[1] = fechaE
    camion[2] = horaE
    camion[3] = minE
    camion[4] = origen
    camion[5] = fechaS
    camion[6] = horaS
    camion[7] = minS

def verPlaca(camion):
    return camion[0]

def verFechaEntrada(camion):
    return camion[1]

def verHoraEntrada(camion):
    return camion[2]

def verMinEntrada(camion):
    return camion[3]

def verOrigen(camion):
    return camion[4]

def verFechaSalida(camion):
    return camion[5]

def verHoraSalida(camion):
    return camion[6]

def verMinSalida(camion):
    return camion[7]

def modPlaca(camion, placaN):# placa nuevo
    camion[0] = placaN

def modFechaEntrada(camion, fechaEN):
    camion[1] = fechaEN

def modHoraEntrada(camion, horaEN): # Hora Entrada Nuevo
    camion[2] = horaEN

def modMinEntrada(camion, minEN): # Minutos Entrada Nuevp
    camion[3] = minEN

def modOrigen(camion, origenN):# Origen nuevo
    camion[4] = origenN

def modFechaSalida(camion, fechaSN):
    camion[5] = fechaSN

def modHoraSalida(camion, horaSN): # Hora Salida Nuevo
    camion[6] = horaSN

def modMinSalida(camion, minSN):# Minuto salida nuevo
    camion[7] = minSN

def copiar(camion1, camion2):
    camion1[0] = camion2[0]
    camion1[1] = camion2[1]
    camion1[2] = camion2[2]
    camion1[3] = camion2[3]
    camion1[4] = camion2[4]
    camion1[5] = camion2[5]
    camion1[6] = camion2[6]
    camion1[7] = camion2[7]