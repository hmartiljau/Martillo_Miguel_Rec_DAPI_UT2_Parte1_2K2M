def process_class(archivo):
    #notas = {}  # Diccionario para almacenar las notas de los alumno
    #with open(archivo, encoding="utf-8") as archivo:
        #lineas = file.readlines()
        #for linea in lineas[1:]:
        # print(lineas)
#archivo="class.csv"
#import os
#def process_class(archivo):
    '''Este función lee un fichero CSV con las notas 
        de un grupo de alumnos/as en una unidad de trabajo 
        de un módulo y los almacene.
        Parámetros:
            - tendremos un str con la ruta del fichero (.csv) a abrir
        Salida:
            -La función no devuelve nada'''
    
    
    notas={}
    with open(archivo, 'r') as file:
            lineas = file.readlines()
            cabecera=lineas.pop(0)
            for linea in lineas:
                notas={linea.replace("\n","")}
                print(notas)
process_class('class.csv')