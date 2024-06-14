#apuntes de programacion
#leer y escribir 06/05/2024

nombre=input("¿cual es tu nombre?")
print("hola , mi nombre es", nombre)


year= input("en que año naciste?")
print("naci en el año",year)


#funciones:

# 1: string 8/05/2024

institucion= "universidad de los lagos"
asignatura= "programacion"
descripcion= "asignatura de primer semestre de la carrera"
print(institucion[1])

#concatenacion
resultado= print(institucion +" "+ asignatura)

#multiplicar texto
palabra= "hola"
resultado= palabra * 2
print(resultado)

#funcion split
print(institucion.split())

#funcion len cuenta indice

print(len(asignatura))

# boleanoos: 10/05/2024
import math

#potencia
estatura=1.70
peso=70
imc=peso / (estatura**2)

print(math.trunc(imc))

print("######## BOOLEANOS ########\n")
ampolleta=False
interruptor= True

print(type (ampolleta),type (interruptor))
print(type(imc))
print(type(peso))

#salidas booleanas
print(1<=0)
print(100>=10)
print(19==19)

#declarando booleanos
print(bool(0))
print(bool(""))
print(bool([]))
print(bool("false"))
print(bool(1))


