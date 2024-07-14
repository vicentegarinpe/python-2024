#ejercicio cadena invertida


cadena = input("Ingresa una cadena de texto: ")
cadena_invertida = ""

for caracter in cadena:
    cadena_invertida = caracter + cadena_invertida

print("Cadena invertida:", cadena_invertida)
