#ejercicios de guia de estudios
#ejercicio 1

#pedir datos de los estudiantes

joeln1=float(input("Ingrese la primera nota de joel: "))
joeln2=float(input("Ingrese la segunda nota de joel: "))
joeln3=float(input("Ingrese la tercera nota de joel: "))

alondra1=float(input("Ingrese la primera notade alondra: "))
alondra2=float(input("Ingrese la segunda notade alondra: "))
alondra3=float(input("Ingrese la tercera nota de alondra: "))

paz1=float(input("Ingrese la primera nota de paz: "))
paz2=float(input("Ingrese la segunda nota de paz : "))
paz3=float(input("Ingrese la tercera notade paz: "))
#calcular promedio de los estudiantes
promediojoel= round((joeln1 + joeln2+ joeln3 )/ 3,3)
promedioalondra= round((alondra1 + alondra2+ alondra3)/ 3,3)
promediopaz= round((paz1+ paz2+paz3 )/ 3,3)

print("el promedio final de joel es:  ",promediojoel)
print("el promedio final de alondra es:",promedioalondra)
print("el promedio final de paz ",promediopaz)

#calculo de minimo
min_dejoel=min(joeln1,joeln2,joeln3)
min_dealondra=min(alondra1,alondra2,alondra3)
min_depaz=min(paz1,paz2,paz3)

#sacar el promedio final de los promedios anteriormente solicitados
promediofinal=round((promedioalondra+promediojoel+promediopaz)/3,3)

#ejercicio 2

descripcion="Estediseñodecuadernosoloestadisponibleenazulyrojo "
caracter=len(descripcion)>50
print(caracter)
print(descripcion[:10])

#ejercicio 3

print("buenos dias a continuacion ordenaremos inventario:\n")

print("Para poder ordenar ingrese una descripcion de minimo 40 letras caracteres")