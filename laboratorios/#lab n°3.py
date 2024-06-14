#lab n°3 

#creamos subdiccionarios con informacion dada
primerdiccionario={
    "Id region": 14,
    "nombre region: ":"LOS RIOS",
    "Superficie(km2): ": 18.429,
    "habitantes (2017): ": 404.432 

}
segundodiccionario={  
    "Id region": 12,
    "nombre region: ":"MAGALLANES",
    "Superficie(km2): ": 1382291 ,
    "habitantes (2017): ": 166.533
    
}

#print a el diccionario
print()
censo_17={
    print(primerdiccionario),
    print(segundodiccionario)
}
#calculamos densidad
densidad1=(round(404432/18429 ,1))
densidad2=(round(166533/1382291,1))

print(f"La densidad de la region de LOS RIOS  es: {densidad1}\n")
print(f"la densidad de la region de MAGALLANES es :{densidad2}\n")


provincias14=("Ranco", "Valdivia")
provincia12=("Antártica Chilena", "magallanes", "Tierra del Fuego","Última Esperanza")

listadecomunas=["Río Bueno", "La Unión", "Paillaco"]
listacomunas12=["Cabo de Hornos", "Puerto Williams","Porvenir"]

#AGREGAMOS COMUNAS Y PROVINCIAS
newprimerdiccionario={
    "Id region": 14,
    "nombre region: ":"LOS RIOS",
    "Superficie(km2): ": 18.429,
    "habitantes (2017): ": 404.432, 
    "capital":"VALDIVIA",
    "comunas": listadecomunas,
    "provincias":provincias14
}
newsegundodiccionario={  
    "Id region": 12,
    "nombre region: ":"MAGALLANES",
    "Superficie(km2): ": 1382291 ,
    "habitantes (2017): ": 166.533,
    "capital":"PUNTA ARENAS",
    "Comunas": listacomunas12,
    "provincias":provincia12
   
}

#cambio de nombre region
newsegundodiccionario2_0={  
    "Id region": 12,
    "nombre region: ":"MAGALLANES Y ANTARTICA CHILENA",
    "Superficie(km2): ": 1382291 ,
    "habitantes (2017): ": 166.533,
    "capital":"PUNTA ARENAS",
    "Comunas": listacomunas12,
    "provincias":provincia12
   
}

print(("###Diccionario actualizado###\n"))
print("###Primer diccionario###\n")
print(newprimerdiccionario)
print("###Segundo diccionario###\n")
print(newsegundodiccionario2_0)





