#ejercicio numero 4 de guia de estudio

import random


numero_a_adivinar = random.randint(1, 100)

print("¡Bienvenido al juego de adivinar el número!")
print("He pensado en un número entre 1 y 100. ¡Intenta adivinarlo!")

while True:

    intento = int(input("Ingresa un número: "))
    
   
    if intento < numero_a_adivinar:
        print("El número a adivinar es mayor.")
    elif intento > numero_a_adivinar:
        print("El número a adivinar es menor.")
    else:
        print("¡Felicidades! Has adivinado el número.")
        break
