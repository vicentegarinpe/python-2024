#ejercicios propuestos
# Tuplas originales
puntajes_matematicas = (55, 17, 93, 75, 88, 55)
puntajes_quimica = (10, 85, 75, 88, 91, 75)
puntajes_programacion = (68, 78, 85, 68, 82, 10)

# A) Imprimir los valores duplicados de cada tupla

# Encontrar duplicados en puntajes_matematicas
vistos_matematicas = set()
duplicados_matematicas = set()
for x in puntajes_matematicas:
    if len(vistos_matematicas) == len(vistos_matematicas.union({x})):
        duplicados_matematicas = duplicados_matematicas.union({x})
    else:
        vistos_matematicas = vistos_matematicas.union({x})
print("Duplicados en Matemáticas:", duplicados_matematicas)

# Encontrar duplicados en puntajes_quimica
vistos_quimica = set()
duplicados_quimica = set()
for x in puntajes_quimica:
    if len(vistos_quimica) == len(vistos_quimica.union({x})):
        duplicados_quimica = duplicados_quimica.union({x})
    else:
        vistos_quimica = vistos_quimica.union({x})
print("Duplicados en Química:", duplicados_quimica)

# Encontrar duplicados en puntajes_programacion
vistos_programacion = set()
duplicados_programacion = set()
for x in puntajes_programacion:
    if len(vistos_programacion) == len(vistos_programacion.union({x})):
        duplicados_programacion = duplicados_programacion.union({x})
    else:
        vistos_programacion = vistos_programacion.union({x})
print("Duplicados en Programación:", duplicados_programacion)

# B) Convertir cada tupla en una lista y ordenar las listas en orden descendente

# Convertir y ordenar lista_matematicas
lista_matematicas = list(puntajes_matematicas)
lista_matematicas.sort()
lista_matematicas = lista_matematicas[::-1]  # Invertir la lista
print("Puntajes Matemáticas ordenados:", lista_matematicas)

# Convertir y ordenar lista_quimica
lista_quimica = list(puntajes_quimica)
lista_quimica.sort()
lista_quimica = lista_quimica[::-1]  # Invertir la lista
print("Puntajes Química ordenados:", lista_quimica)

# Convertir y ordenar lista_programacion
lista_programacion = list(puntajes_programacion)
lista_programacion.sort()
lista_programacion = lista_programacion[::-1]  # Invertir la lista
print("Puntajes Programación ordenados:", lista_programacion)

# C) Unir las listas anteriormente generadas en una sola y eliminar los duplicados
lista_unida = lista_matematicas + lista_quimica + lista_programacion
lista_unida_sin_duplicados = []
vistos = set()
for x in lista_unida:
    len_vistos_antes = len(vistos)
    vistos = vistos.union({x})
    if len_vistos_antes != len(vistos):
        lista_unida_sin_duplicados.append(x)
print("Lista unida sin duplicados:", lista_unida_sin_duplicados)

# D) Encontrar el puntaje máximo y mínimo de la lista resultante
puntaje_maximo = lista_unida_sin_duplicados[0]
puntaje_minimo = lista_unida_sin_duplicados[0]

for x in lista_unida_sin_duplicados:
    if x > puntaje_maximo:
        puntaje_maximo = x
    if x < puntaje_minimo:
        puntaje_minimo = x

print("Puntaje máximo:", puntaje_maximo)
print("Puntaje mínimo:", puntaje_minimo)
