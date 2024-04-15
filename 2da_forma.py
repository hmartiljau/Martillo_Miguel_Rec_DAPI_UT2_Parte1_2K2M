def process_class(archivo):
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

            for linea in lineas[1:]:
                #campos=linea.strip().split(',')
                alumno=linea.replace("\n","").split(',',maxsplit=2)
                #practicas=alumno[2].split(',')
                #unir=','.join(practicas)
                #a=unir.replace('","', '.')
                sep_notas=alumno[2].replace('","', '"."').split('.')

                #notasprac=",".join(campos[2::])
                #sus=(campos[2::])
                #com=sus.split('"')
                #nombre=campos[:1]
                #nombres=",".join(campos[::1]
                
                nombre=alumno[0]
                apellido=alumno[1]
                practica01=sep_notas[0]
                practica02=sep_notas[1]
                practica03=sep_notas[2]
                examen=sep_notas[3]
                recuperacion=sep_notas[4]
                actitud=sep_notas[5]
                notas = {
                    "nombre": nombre,
                    "apellido": apellido, 
                    "Practica01": practica01,
                    "Practica02": practica02,
                    "Practica03": practica03,
                    "Examen": examen,
                    "Recuperacion": recuperacion,
                    "Actitud": actitud
                    
                }
                print (notas)
process_class("class.csv")
