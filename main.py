import functools
from queue import PriorityQueue
from textwrap import indent
from dao import *
from ui import *
from services.covidapi import Covidapi
import json
#-------------------MUNE--------------------
opcion = 'M' #<---bucle infinito para volver a mostrar

while(opcion != 'S'): #<-- como es 'M' si ponesmos en consola 'S' se sale 
    if (opcion == 'M'):
        print("m")
    elif (opcion == 'Z'):
        crear_tabla_query()
        crear_tabla_data()
        ingreso = 'H'
        while(ingreso != 'L'):
            pais = input("Ingrese la Pais: Ejemplo(HND,MEX):")
            fecha = input("Ingrese la fecha: Ejemplo(2022-07-17):")
            pais_prueba = pais
            fecha_prueba = fecha
            print(verificar(pais_prueba ,fecha_prueba))
            x = (pais_prueba,fecha_prueba)
            print(x)
            separador()
            
            if (x == verificar(pais_prueba,fecha_prueba)):
                print("si esta el registro")
                ingreso = 'H'
            else:
                print("no esta no esta el registro")
                ingreso = 'L'

        covidApi = Covidapi()
        #pais = "MEX"
        #fecha = "2022-07-17"
        print("APIQuery", pais, fecha, sep="\t")
        print("="*40)
        apiData = covidApi.getReports(pais, fecha)
        #print(json.dumps(apiData, indent=4))
        añadir_tabla_query(pais,fecha)

        
        
        print(verificar_id_ver(pais,fecha))
        id_para_llamar = verificar_id_ver(pais,fecha)
        res = functools.reduce(lambda sub, ele: sub * 10 + ele, id_para_llamar)
        print(res)


        arr_data = apiData["data"]
        for data_item in arr_data:
            
            confirmed = data_item["confirmed"]
            #idquery = data_item["Id_Query"]
            active = data_item["active"]
            province = data_item["region"]["province"]
            print(confirmed, active, province, sep="\t")
            añadir_tabla_data(res,confirmed,active,province)
            
    elif (opcion == 'Q'):
        
        table_row(mostar_tabla_query())
    elif (opcion == 'D'):
        table_row_date(mostrar_tabla_data())
    elif (opcion == 'Y'):
        selecc = int(input("Ingrese la llave foranea de los registros almacenados : "))
        table_row_date(selecionar_id(selecc))
    elif(opcion == 'V'):
        sss = "MEX"
        fff = "2021-05-05"
        print(verificar_id_ver(sss,fff))
        id_para_llamar = verificar_id_ver(sss,fff)
        res = functools.reduce(lambda sub, ele: sub * 10 + ele, id_para_llamar)
        print(res)

    else:
        print("No existe opción")
    opcion = menu().rstrip().lstrip().upper()






