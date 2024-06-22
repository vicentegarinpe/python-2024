
""""
     edad no valida < 0
     niño/a <=12
     adolescente <=17
     adulto <=120
     edad no valida >= 120
"""
edad2_0=int(input("ingrese su edad: "))

if edad2_0<0 or edad2_0 <=120:
    categoria="edad no valida"
elif edad2_0<=12:
    categoria="niño/a"
elif edad2_0<=64:
    categoria="adulto"
else:
    categoria="adulto mayor"

print(f"la persona es: {categoria}")