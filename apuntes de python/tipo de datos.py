#listas

#declarar listas

ciudades=["castro","queilen","ancud","quellon","chonchi","castro"]
varios=["nicolas",20,True]

#otra forma de inicilizar lista

lista2=list(["python","ruby"])
print(ciudades)
print(type(ciudades))
print(len(ciudades))

print(ciudades.count("castro"))

listanum= [0,1,2,3,4,5,6,7,8,9,10] #impresion lista normal
listnum2=list(range(1,11))  #impresion de lista con range

print(listanum)
print(listnum2)

# tuplas
musica=tuple()
generos=("rock","regueton","rap","hip-pop")

print(generos)
print(type(generos))

print(generos[3])

print(generos.index("hip-pop"))


lista=[1,2,3,4,5,6,7,8,9,10]
listnum=list(range(1,1000,10))

print(listnum)
print(lista)

# tuple son inmutables no se puede cambiar algo que este adentro como las listas
musica=tuple()
generos=("rock","regueton","rap","hip-pop")

print(generos)
print(type(generos))
print(generos[3])
print(generos.index("hip-pop"))

#cambio de estructura de tupla a lista

tuplitas=("victor",20 ,"universidad ", True )
print(tuplitas)
tuplitas=list(tuplitas)
print("la tupla ahora es tipo",type(tuplitas))

#tomando trozo de una tupla 
print(tuplitas[0:3])

""""                      sets(conjuntos)                    """

conjunto_vacio=set()
conjunto_x={} 
#print sets
print(type(conjunto_x))
print(type(conjunto_vacio))

#funciones de sets 
#add()
#clear()
#discard()
colores={"azul","rojo","amarillo","verde"}
animales=list({"guacamayo", "gato", "perro", "hamster"})

print(colores)
print(animales)
#agregando nuevo elemento al set
print(colores.add("celeste"))

print(colores)


# diccionarios                                              

paciente={                             # forma mas usada de diccionario
    "nombre": "alfredo",
    "edad":29,
    "ciudad":"osorno"
    }


hospital=dict(                        # otra forma de inicializar dict
    nombre="hospital de castro",
    direccion="franscisco silva 961",
    ciudad="caastro"
)

print(type(paciente))
print(type(hospital))

print(paciente,hospital)