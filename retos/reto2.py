#reto numero 2
nombre_estudiante=str(input("Ingrese su nombre: "))

#asignatura1
nombre_asignatura1=str(input("Ingrese el nombre de la asignatura 1: "))
asignatura1_lab1=float(input("Ingrese la nota del primer laboratorio de la primera asignatura:"))
asignatura1_lab2=float(input("Ingrese la nota del segundo laboratorio de la primera asignatura: "))
asignatura1_lab3=float(input("Ingrese la nota del tercer laboratorio de la primera asignatura: \n"))

#asignatura2
nombre_asignatura2=str(input("Ingrese el nombre de la asignatura 2: "))
asignatura2_lab1=float(input("Ingrese la nota del primer laboratorio de la segunda asignatura :"))
asignatura2_lab2=float(input("Ingrese la nota del segundo laboratorio de la segunda asignatura:"))
asignatura2_lab3=float(input("Ingrese la nota del tercer laboratorio de la segunda asignatura: \n"))

#asignatura3
nombre_asignatura3=str(input("Ingrese el nombre de la asignatura 3: "))
asignatura3_lab1=float(input("Ingrese la nota del primer laboratorio de la tercera asignatura: "))
asignatura3_lab2=float(input("Ingrese la nota del segundo laboratorio de la segunda asignatura:  "))
asignatura3_lab3=float(input("Ingrese la nota del tercer laboratorio de la tercera asignatura: \n"))


nombreasig=tuple({nombre_asignatura1,nombre_asignatura2,nombre_asignatura3})
notalab1=tuple({asignatura1_lab1,asignatura2_lab1,asignatura3_lab1})
notaslab2=tuple({asignatura1_lab2,asignatura2_lab2,asignatura3_lab2})
notaslab3=tuple({asignatura1_lab3,asignatura2_lab3,asignatura3_lab3})



    

#ponderacion asignatura 1 
ponderacionlab1asig1=asignatura1_lab1*0.30
ponderacionlab2asig1=asignatura1_lab2*0.50
ponderacionlab3asig1=asignatura1_lab3*0.20

promedio_totalasignatura1=(round(ponderacionlab1asig1+ponderacionlab2asig1+ponderacionlab3asig1))

#ponderacion asignatura 2
ponderacionlab1asig2=asignatura2_lab1*0.30
ponderacionlab2asig2=asignatura2_lab1*0.50
ponderacionlab3asig2=asignatura2_lab1*0.20

promedio_totalasignatura2=(round(ponderacionlab1asig2+ponderacionlab2asig2+ponderacionlab3asig2,1))
#ponderacion asignatura 3
ponderacionlab1asig3=asignatura2_lab1*0.30
ponderacionlab2asig3=asignatura2_lab1*0.50
ponderacionlab3asig3=asignatura2_lab1*0.20

promedio_totalasignatura3=(round(ponderacionlab1asig3+ponderacionlab2asig3+ponderacionlab3asig3,1))

#ocupamos diccionario

asig1={                            
    "Nombre":(nombre_estudiante),
    "Nombre asignatura ":(nombre_asignatura1),
    "Nota laboratorio 1":(asignatura1_lab1),
    "Nota laboratorio 2":(asignatura1_lab2),
    "Nota laboratorio 3":(asignatura1_lab3),
    "Promedio final":(promedio_totalasignatura1)
    }

asig2={                           
    "Nombre":(nombre_estudiante),
    "Nombre asignatura":(nombre_asignatura2),
    "Nota laboratorio 1":(asignatura2_lab1),
    "Nota laboratorio 2":(asignatura2_lab2),
    "Nota laboratorio 3":(asignatura2_lab3),
    "Promedio final":(promedio_totalasignatura2)
    }

asig3={                             
    "Nombre": (nombre_estudiante),
    "Nombre asignatura ":(nombre_asignatura3),
    "Nota laboratorio 1: ":(asignatura3_lab1),
    "Nota laboratorio 2: ":(asignatura3_lab2),
    "Nota laboratorio 3: ":(asignatura3_lab3),
    "Promedio final de la asignatura: ":(promedio_totalasignatura3)
    }

diicciio={
    nombre_estudiante:[asig1,
                    asig2 ,
                    asig3]
}


print(diicciio[nombre_estudiante])