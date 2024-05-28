#ejercicio o repaso 

#declarar numero correcto
numerocorrecto=20

#pedir un nunmero al usuario
numerodado=int(input("¿puedes intentar adivinar el numero que pienso del 1 al 100?"))

#while como un mientras se cumpla esto pasara otra cosa
while numerodado!= numerocorrecto:
    if numerodado>numerocorrecto:
     print("EL NUMERO ES DEMASIADO ALTO PRUEBA OTRO")
    
    elif numerodado< numerocorrecto:
     print("EL NUMERO ES MUY BAJO PRUEBA OTRO")
    

    numerodado=int(input("ingresa el numero de nuevo:"))

print("LO ADIVINASTE")