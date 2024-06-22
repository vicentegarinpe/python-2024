#ejercicio n1 guia 3 listo

# Definir el párrafo
parrafo = """
La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus
pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion
democratica.
"""

# Convertir el párrafo a minúsculas y contar las repeticiones de "universidad"
cantidad_universidad = parrafo.count("universidad")

# Crear la tupla con la palabra "universidad" repetida
palabras_encontradas = ("universidad",) * cantidad_universidad

# Imprimir resultados
print(f"La palabra 'universidad' se repite {cantidad_universidad} veces.")
print(f"Palabras encontradas: {palabras_encontradas}")
