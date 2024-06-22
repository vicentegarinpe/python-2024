import random
# Generar los numeros random
numeros = [random.randint(40, 350) for _ in range(20)]

# Mostrar los numeros
print("Números generados:", numeros)

# pedir ingresar numero a buscar
numero_buscado = int(input("Ingrese el número para buscar en la lista: "))

# Contar los repetidos
repetidos = numeros.count(numero_buscado)

# Mostrar el resultado
print(f"El número {numero_buscado} aparece {repetidos} veces en la lista.")

