#hacer lista de los animales
listadepalabras=["pelicano","guacamayo","gato","lagartijas","camello"]

#elegi al animal y lo puse en una variable para despues poder despues contar la cantidad de letra
animalescondido=listadepalabras[1]

#con la variable anteriormente hecha ahora con len cuenta la cantidad de letras
cantidadletraanimal=len(animalescondido)

#pedimos el primer intento al jugador
print("HOLA HOY INTENTARAS ADIVINAR CUAL ANIMAL ESTOY PENSANDO PERO POR LA CANTIDAD DE LETRAS LAS ALTERNATIVAS SON:")
print("pelicano , guacamayo, gato, lagartijas, camello ")
animaldado=str(input("porfavor intenta adivinar entre estos animales cual estoy pensando:"))

while animalescondido!=animaldado:
    if animalescondido>animaldado:
        print("Te doy una pista: Este animal tiene mas letras")
    elif animalescondido<animaldado:
        print("Te doy una pista : Este animal tiene menos letras")

    animaldado=str(input("ingresa otro animal:"))

print("haz acertado la cantidad de letras y el animal el cual es:",animalescondido)