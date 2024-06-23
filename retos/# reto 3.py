# reto 3

ciudades=["santiago","temuco","osorno","punta arenas"]
indicecalidaddeaire=[134,99,245,50] 

indice_minimo = min(indicecalidaddeaire)
indice_maximo = max(indicecalidaddeaire)

# Encontrar las ciudades correspondientes
ciudad_minima = ciudades[indicecalidaddeaire.index(indice_minimo)]
ciudad_maxima = ciudades[indicecalidaddeaire.index(indice_maximo)]

#encontrar
if 0 <= indice_minimo <= 50:
    categoria_minimo = "Buena"
elif 51 <= indice_minimo <= 100:
    categoria_minimo = "Moderada"
elif 101 <= indice_minimo <= 150:
    categoria_minimo = "Dañina a la salud para grupos sensibles"
elif 151 <= indice_minimo <= 200:
    categoria_minimo = "Dañina a la salud"
elif 201 <= indice_minimo <= 300:
    categoria_minimo = "Muy dañina a la salud"
else:
    categoria_minimo = "Peligrosa"


if 0 <= indice_maximo <= 50:
    categoria_maximo= "Buena"
elif 51 <= indice_maximo <= 100:
    categoria_maximo = "Moderada"
elif 101 <= indice_maximo <= 150:
    categoria_maximo = "Dañina a la salud para grupos sensibles"
elif 151 <= indice_maximo <= 200:
    categoria_maximo = "Dañina a la salud"
elif 201 <= indice_maximo <= 300:
    categoria_maximo = "Muy dañina a la salud"
else:
    categoria_maximo = "Peligrosa"

print(f"La ciudad con el índice de calidad del aire más bajo es {ciudad_minima} con un índice de {indice_minimo}, que es {categoria_minimo}.")
print(f"La ciudad con el índice de calidad del aire más alto es {ciudad_maxima} con un índice de {indice_maximo}, que es {categoria_maximo}.")
