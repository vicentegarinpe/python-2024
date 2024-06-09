#ejercicio3

aves={"aguila","canario","pato"}
animales_terrestres={"leon","elefante","nutria"}
animales_acuaticos={"pato","delfin","nutria"}

print(f"aves: {aves}")
print(f"animal esterrestres: {animales_terrestres}")
print(f"animales acuaticos: {animales_acuaticos}")

aves.add("pelicano")
animales_terrestres.add("lobo")
animales_acuaticos.add("pez espada")

print(f"aves: {aves}")
print(f"animal esterrestres: {animales_terrestres}")
print(f"animales acuaticos: {animales_acuaticos}")

intersectionaves=aves.intersection(animales_terrestres)
interseccionterrestres=aves.intersection(animales_acuaticos)
intersectionacuaticos=animales_terrestres.intersection(animales_acuaticos)

print(f"aves y animales terrestres:{intersectionaves}")
print(f"aves y acuaticos:{interseccionterrestres}")
print(f"acuaticos y terrestres:{intersectionacuaticos}")
 





