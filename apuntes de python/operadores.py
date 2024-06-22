#comparando cadenas de caracteres
animaldomestico="gato"
animalessalvaje="pato"
print(animaldomestico!=animalessalvaje)
print(animaldomestico!=animalessalvaje)
print(animaldomestico>animalessalvaje)
print(animaldomestico<animalessalvaje)


#if
edad=19
if edad>=18:
    print("eres mayor de edad\n")
else:
    print("eres menor de edad\n")
print("otro texto\n")


#bucles y condicionales
bencina=True
encendido=True
edad=19

#utilizando el operador and( IF ES UN SI Y ELSE ES UN SINO)
if bencina and encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede arrancar")

if bencina or encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede arrancar")
if not bencina and encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede arrancar ")

#operadores ternarios
edad_2=19
print("usted puede votar"if edad_2>=18 else "usted no puede votar")

#bucles
num=0
while num<=100:
    print(num)
    num+=2

#combinacion de while y else
while num <=100:
    print(num)
    num+=2
else:
    print("mi variable es igual o mayor a 100")

while True:
    parametro=input(">")
    if parametro== "exit":
        break
    else:
        print(parametro)




