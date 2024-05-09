"""
------Especificación: 

    • Nombre del TAD: TAD Empresa (archivo TAD_Empresa.py)
    • Sirve para almacenar los distintos cmaiones que ingresen al centro
    • Operaciones Básicas:
    
#def crearEmpresa()
    Crea una empresa vacia

#def agregarCamion(emp, camion)
    Agrega un camion a la empresa

#def eliminarAuto(emp, camion)
    Elimina un camion de la empresa

#def tamanio(emp)
    Devuelve el tamaño de la empresa

#def recuperarCamion(emp, i)
    Retorna el auto en la posicion iesima ??



------Estructura Interna:
emp = [camion] 
camion=[placa, horaE, minE, origen, horaS, minS]
camion = ["",0,0,"", 0,0]

"""

from TAD_Camion import*

def crearEmpresa():
    emp = []
    return emp  

def agregarCamion(emp, camion):
    emp.append(camion)

def eliminarCamion(emp, camion):
    emp.remove(camion)

def tamanio(emp):
    return len(emp)

def recuperarCamion(emp, i):
    return emp[i]

# def existeCamion(emp, camion):
#     return camion in emp