palabras = input("Ingrese una cadena de 150 caracteres: ")
palabras = palabras.lower()

while len(palabras) != 150:
    print("La cadena debe tener exactamente 150 caracteres. Inténtalo de nuevo.")
    palabras = input("Ingrese una cadena de 150 caracteres: ")
    palabras = palabras.lower()  #  cadena sea en minúsculas

contador = 0

for caracter in palabras:
    if caracter == 'a':  # Aquí comparas cada caracter con 'a'
        contador += 1

print(f"El carácter 'a' se repite {contador} veces.")

