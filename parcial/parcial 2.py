#parcial 2 
#ejercicio 1
TemperaturasMínimas = {9, 5, 2, 7, 6, 1}
TemperaturasMáximas = {12, 14, 11, 10, 15, 9}

#a (mas o menos)
if 9 > len(TemperaturasMínimas):
    print("la temperatura 9° si se encuentra entre las temperaturas minimas.")
else:
    print("no se encuentra")
    

if 9 < len(TemperaturasMáximas):
    print("la temperatura 9° si se encuentra entre las temperaturas maximas.")
else:
    ("La temperatura no se encuentra") 

#b (listo)
union=set(TemperaturasMáximas.union(TemperaturasMínimas))

print(f"la union  de los dos set es {union}")

#c listas (no utilize bucles )
min_alista=[TemperaturasMínimas]
lista_max=[TemperaturasMáximas]

#d crear tupla con los valores de temperatura min y max

temperatura_minima=min(TemperaturasMínimas)
temperatura_maxima=max(TemperaturasMáximas)
atupla=(temperatura_minima)
atupla2=(temperatura_maxima)
print(f"la temperatura minima es :{atupla}")
print(f"la temperatura maxima es :{atupla2}")

#e (listo)
diccinario={
    "temperaturas minimas": TemperaturasMínimas,
    "temperaturas maximas": TemperaturasMáximas
}

print(diccinario)


#ejercicio 2


palabra = input("Ingresa una palabra: ")

palabra_limpia = ''.join(palabra.split()).lower()


palabra_invertida = ''
for caracter in palabra_limpia:
    palabra_invertida = caracter + palabra_invertida

# Verificar si es un palíndromo
es_palindromo = palabra_limpia == palabra_invertida


print("Palabra invertida:", palabra_invertida)


if es_palindromo:
    print("La palabra ingresada es un palíndromo.")
else:
    print("La palabra ingresada no es un palíndromo.")
