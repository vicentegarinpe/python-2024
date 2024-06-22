#ejercicio n°1 de guia 3

# Definir el párrafo
parrafo = """
La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus
pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion
democratica.
"""

#poner en minusculas para igualar palabras
parrafo_igualado = parrafo.lower()

# Contar las repeticiones de la palabra "universidad"
cantidad_universidad = parrafo_igualado.count("universidad")

# Crear la tupla 
palabras_encontradas = ("universidad",) * cantidad_universidad

# Imprimir la cantidad y la tupla
print(f"La palabra 'universidad' se repite {cantidad_universidad} veces.\n")
print(f"Palabras encontradas: {palabras_encontradas}")