#variables
# IF

#Ejemplo:
edad1 = 19

if edad1 >= 18:
    print("eres mayor de edad.")
else:
    print("eres menor de edad.")
print("Este print esta fuera del if") # <--- no se indentó (indentar), por ende no funcionara dentro del if

# Ejemplo 2:
edadagustin = 18

if edadagustin >= 18 and edadagustin < 65:
    print("Eres mayor de edad")
elif edadagustin > 65:
    print("eres un adulto mayor.")
else:
    print("Eres menor de edad")

# Inicializamos las variables
numero = 10
suma = 0

# Mientras el número sea menor o igual a 50
while numero <= 50:
    suma += numero # Sumamos el número actual a la suma total
    numero += 2 # Incrementamos el número en 2

# Imprimimos la suma total
print("La suma de los números del rango 10 al 50, incrementando de 2 en 2, es:", suma)

#              OPERADORES TERNARIOS
"""
El operador ternario permite hacer una condicion con una sola linea.


"""
edad3 = 20

print("Usted puede votar" if edad1 >= 18 else "Usted no puede votar."        ) # <-- los programadores senior ocupan esto.


#         BUCLES/CICLOS/LOOPS



#         while (mientras)
"""
Este tipo de ciclo permite ejecutar


"""


#WHILE INFINITO (NO HACER):

# while True
#   print(num)                  <--- NO HACER ESTO ya que es un bucle infinito, en resumenno tiene un termino.
#   num +=2

#                        ctrl + c | para salir de un bucle infinito.


#                    WHILE (ELSE/IF)
num = 20
while num <= 100:
    print(num)
    num += 2
else:
    print("mi variable es igual o mayor a 100")


while True:
    parametro = input(">")
    if parametro == "exit": # <-- hasta que yo escriba "exit" en terminal
        break
    else:
        print(parametro)



"""
    edad no valida < 0
    niño/a <= 12
    adolecente <= 17
    adulto <=64
    adulto mayor <= 120
    Edad no válida >= 120
"""

edad = int(input("ingrese la edad de la persona: "))

if edad <= 0 or edad >= 120:
    categoria = "Edad no válida"
elif edad <= 12:
    categoria = "Niño/a"
elif edad <= 17:
    categoria = "adolecente"
elif edad <= 65:
    categoria = "adulto"
else:
    categoria = "adulto mayor"

print(f"La persona es: {categoria}")