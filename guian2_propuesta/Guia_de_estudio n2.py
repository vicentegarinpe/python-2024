#Ejercicio 1
b1 = input("Debera ingresar 4 marcas de bebidas, ingrese la primera: ")
b2 = input("ingrese la segunda: ")
b3 = input("ingrese la tercera: ")
b4 = input("ingrese la cuarta: ")

l1 = [b1,b2,b3,b4]
print(l1)
u = l1[0]
p = l1[-1]
print(u,p)

#Ejercicio 2
print("Ingrese la fecha de vencimiento de 3 productos")
p1 = int(input("\nIngrese el día del primer producto: ")), int(input("Ingrese el mes: ")), int(input("Ingrese el año: "))
p2 = int(input("\nIngrese el día del segundo producto: ")), int(input("Ingrese el mes: ")), int(input("Ingrese el año: "))
p3 = int(input("\nIngrese el día del tercer producto: ")), int(input("Ingrese el mes: ")), int(input("Ingrese el año: "))

fv = (p1, p2, p3)

of = (sorted(fv))
print(of)

#Ejercicio 3
aves = {"Aguila", "Pato", "Canario"}
at = {"Leon", "Nutria", "Elefante"}
aa = {"Delfin", "Pato", "Nutria"}

aves.add("Loro")
print(aves)
t = aves.intersection(aa)
t2 = at.intersection(aa)
print(t)
print(t2)

#ejercicio 4
print("Se le solicitara ingresas 3 nombres y sus edades")
di1 = dict(
    nombre = input("\nIngrese el primer nomnbre: "),
    edad = input("Ahora ingrese su edad: "),
    nombre2 = input("\nIngrese el segundo nomnbre: "),
    edad2 = input("Ahora ingrese su edad: "),
    nombre3 = input("\nIngrese el tercer nomnbre: "),
    edad3 = input("Ahora ingrese su edad: ")
)
print(di1.values())
di1.pop("nombre")
di1.pop("edad")
print(di1.values())
di1.update(
    nombre4= input("Ingresa otro nombre: "),
    edad4= int(input("Ingresa edad: "))
)
print(di1)

#ejercicio 5
print("Debera ingresar 3 ciudades junto a su respectiva latitud y longitud")

c1 = input("\nIngrese la primera ciudad: ")
c1l = float(input("Ingrese la latitud(y): "))
c1lo = float(input("Ingrese la longitud(x): "))
co = (c1l,c1lo)

print(f"La primera ciudad {c1} tiene la latitud {c1l} y su longitud es {c1lo}")
print(f"Sus coordenadas (x,y) son {(co)}")

c2 = input("\nIngrese la segunda ciudad: ")
c2l = float(input("Ingrese la latitud(y): "))
c2lo = float(input("Ingrese la longitud(x): "))
co2 = (c2l,c2lo)

print(f"La segunda ciudad {c2} tiene la latitud {c2l} y su longitud es {c2lo}")
print(f"Sus coordenadas (x,y) son {int(co2)}")

c3 = input("\nIngrese la tercera ciudad: ")
c3l = float(input("Ingrese la latitud(y): "))
c3lo = float(input("Ingrese la longitud(x): "))
co3 = (c3l,c3lo)

print(f"La tercera ciudad {c3} tiene la latitud {c3l} y su longitud es {c3lo}")
print(f"Sus coordenadas (x,y) son {int(co3)}")

l1 = [c1, c2, c3]
t1 = {co, co2,co3}

#ejercicio 6
# a
palabras_claves = []
print("Ingrese 5 palabras claves:")

for i in range(5):
    palabra = input(f"Palabra {i+1}: ")
    palabras_claves.append(palabra)

# b
palabras_unicas = list(set(palabras_claves))

# c
print("Lista original de palabras claves:", palabras_claves)
print("Lista sin duplicados:", palabras_unicas)

#ejercicio7

# a
estudiantes = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    carrera = input(f"Ingrese la carrera del estudiante {i+1}: ")
    nota1 = float(input(f"Ingrese la nota del primer laboratorio del estudiante {i+1}: "))
    nota2 = float(input(f"Ingrese la nota del segundo laboratorio del estudiante {i+1}: "))
    
    # b
    estudiantes[nombre] = (carrera, (nota1, nota2))

# c
for nombre, datos in estudiantes.items():
    carrera, notas = datos
    print(f"Estudiante: {nombre}")
    print(f"Carrera: {carrera}")
    print(f"Notas: {notas}")
    print("------")

