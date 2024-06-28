#segundo ejercicio propuesto
cadena = input("Introduce una cadena de texto: ").lower()  # Convertir a minúsculas para simplificar la comparación

# Inicializar contadores para cada vocal
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

# Recorrer la cadena de texto y contar las vocales
for caracter in cadena:
    if caracter == 'a':
        contador_a += 1
    elif caracter == 'e':
        contador_e += 1
    elif caracter == 'i':
        contador_i += 1
    elif caracter == 'o':
        contador_o += 1
    elif caracter == 'u':
        contador_u += 1

# Imprimir los resultados
print("Número de veces que aparece 'a':", contador_a)
print("Número de veces que aparece 'e':", contador_e)
print("Número de veces que aparece 'i':", contador_i)
print("Número de veces que aparece 'o':", contador_o)
print("Número de veces que aparece 'u':", contador_u)


# ejercicio 3
cadena = input("Introduce una cadena de texto: ")

# Inicializar una cadena vacía para almacenar la cadena invertida
cadena_invertida = ""

# Recorrer la cadena original desde el final hasta el principio
for caracter in cadena:
    cadena_invertida = caracter + cadena_invertida

# Mostrar la cadena invertida
print("Cadena invertida:", cadena_invertida)
