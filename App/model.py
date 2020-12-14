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
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import minpq as pq
from DISClib.ADT import orderedmap as om
from DISClib.ADT import list as lt
from DISClib.ADT import minpq as pq
from DISClib.DataStructures import edge as e
from DISClib.DataStructures import listiterator as it
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Utils import error as error
from DISClib.ADT import graph as gr
from DISClib.ADT import stack as st
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------

def newAnalyzer():

    analyzer = {"Company": None,
                "Total_Taxis": [],
                "Total_Companys": None,
                "DateIndex": None,
                "graph": None}

    analyzer["Company"] = m.newMap(comparefunction=compareMap)
    
    analyzer["Total_Companys"] = 0

    analyzer["DateIndex"] = om.newMap(omaptype= "RBT",
                                      comparefunction=compareDates)


    return analyzer
    

# Funciones para agregar informacion al grafo

def addLine(analyzer, line):
    addCompany(analyzer, line)
    return analyzer      



def addCompany(analyzer, tripfile):

    Map = analyzer["Company"]
    company = tripfile["company"]
    taxiID = tripfile["taxi_id"]
    lsttaxis = analyzer["Total_Taxis"]
    if company == None or company == "" or company == " ": 
        company = "Independent Owner"  
    existcompany = m.contains(Map, company)
    if existcompany:
        consulta = m.get(Map, company)['value']
        consulta["Services"] += 1
        if taxiID not in consulta["Taxis"]:
            consulta["Taxis"].append(taxiID)
            consulta["numTaxis"] +=1
    else:
        analyzer["Total_Companys"] += 1
        DictCompany = newCompany()
        m.put(Map, company, DictCompany)
        m.get(Map, company)['value']["Services"] += 1
    if taxiID not in lsttaxis: 
            lsttaxis.append(taxiID)



# ==============================
# Funciones de consulta
# ==============================

# ==============================
# Funciones Helper
# ==============================

def newCompany():
    num = {"Taxis": [],"numTaxis":0, "Services": 0}
    return num

# ==============================
# Funciones de Comparacion
# ==============================

def compareIds(Id1, Id2):
    if (Id1 == Id2):
        return 0
    elif Id1 > Id2:
        return 1
    else:
        return -1

def compareDates(date1, date2):
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareStations(stop, keyvaluestop):
    stopcode = keyvaluestop['key']
    if (stop == stopcode):
        return 0
    elif (stop > stopcode):
        return 1
    else:
        return -1

def compareMap(keyname,company):
    companyentry=me.getKey(company)
    if keyname == companyentry:
        return 0
    elif keyname>companyentry:
        return 1
    else:
        return -1