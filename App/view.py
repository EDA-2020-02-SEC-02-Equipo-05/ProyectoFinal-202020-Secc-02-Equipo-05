"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________


s = "taxi-trips-wrvz-psew-subset-small.csv"
m = "taxi-trips-wrvz-psew-subset-medium.csv"
l = "taxi-trips-wrvz-psew-subset-large.csv"

# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("\n")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de Taxis")
    print("3- Reporte general de la compañia")
    print("4- Obtener el mejor horario para Chicago")
    print("0- Salir")



def optionTwo():
    print("¿Que archivo quiere cargar?")
    file = input("Escriba 1 para el pequeño.\nEscriba 2 para el mediano.\nEscriba 3 para el grande.\n")
    print("\nCargando información de taxis en Chicago")
    if file[0] == "1":
        controller.loadFile(cont,s)
        print("Archivo cargado")
    elif file[0] == "2":
        controller.loadFile(cont,m)
        print("Archivo cargado")
    elif file[0] == "3":
        controller.loadFile(cont,l)
        print("Archivo cargado")
    else:
        print("Ingrese un valor válido")

def optionThree():
    finale = (controller.all(cont, n))
    
    print("El total de taxis es: "+str(r[0]["Total_Taxis"]))
    print("El total de compañias es: "+str(r[0]["Total_Companys"]))
    if n <= finale[0]["Total_Companys"]:

        print("El top " + str(n) + "compañias por numero de taxis es:")
        for i in (r[1][0]): 
            print(str(i)+" " + str(r[1][0][i]["company"]) + "con" + str(r[1][0][i]["key"]) + " axis")

        print("El top "+str(n) + " compañias por numero de servicios es: ")
        for i in (r[1][1]): 
            print(+str(i) + str(r[1][1][i]["company"]) + "con" + str(r[1][1][i]["key"]) + "servicios")
    else: 
        print("El numero seleccionado no es valido")

def optionFour():
    startingArea = float(input ("ingrese Area inicio: "))
    endingArea = float(input ("ingrese Area final "))

    startingH= input("Ingrese hora de incio del rango (HH:MM):  ")
    endingH = input("Ingrese hora final del rango (HH:MM):  ")

    info = controller.getMejorH(cont,startingArea,endingArea,startingH,endingH)

        if info[1] is not None:
            print("El mejor horario para tomar el viaje es {}, el cual te tomará aproximadamente {} minutos".format(info[0],int(info[2])//60))
            print("La mejor ruta para tomar es {}:".format("/".join(info[1])))
        else:
            print("Lo sentimos, marcó una opcion que no es valida.")



"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar \n')
    if int(inputs[0]) == 1:
        print('\nInicializando...')
        cont = controller.init()
    elif int(inputs[0]) == 2:
        optionTwo()
    elif int(inputs[0]) == 3:
        optionThree()
    elif int(inputs[0]) == 4:
        optionFour()
    else:
        sys.exit(0)
