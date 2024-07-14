#ejercicio 1 

#creamos variables de precio unitario y cantidad
manzanapu=100
perapu=250
duraznopu=300
#cantidad
cantidadman=150
cantidadpera=80
cantidaddurazno=120

#total a pagar por cada fruta comprada
CLPmanzana=(manzanapu*cantidadman)
CLPera=(perapu*cantidadpera)
CLPdurazno=(duraznopu*cantidaddurazno)

#suma del total de pera y manzana

sumatotalperaymanzana=(CLPmanzana+CLPera)

#calculo de min
min_total=min(CLPera,CLPdurazno,CLPmanzana)
#calculo de max
max_total=max(CLPera,CLPdurazno,CLPmanzana)

#calcular promedio de precio unitario
promediopu=(manzanapu+perapu+duraznopu )/3

#Mostramos los datos requeridos en pantalla
print("Buenos dias a continuacion conocera el total a pagar por cantidad de cada fruta comprada\n")

print(f"La suma total a pagar por manzana es : {CLPmanzana} CLP")

print(f"la suma total a pagar por la pera es : {CLPera} CLP")

print(f"la suma total a pagar por el durazno es : {CLPera} CLP \n")

print(f"La suma total a pagar por manzanas y peras es: {sumatotalperaymanzana} CLP\n")

print(f"El valor máximo entre los tres precios totales es: {max_total} CLP\n")
print(f"El valor mínimo entre los tres precios totales es: {min_total} CLP\n")

print("El promedio del precio unitario de todas las frutas es:\n",promediopu)




#ejercicio 2
#ejercicio 2

print("Esto un módulo que permite que ingrese un articulo a continuacion...\n ")
#pedimos por cosola el breve resumen 
descripcion=str(input("Ingresar un breve resumen del artículo igual o menor a 60 caracteres: "))[:60]
caracteres=len(descripcion)

# 
while descripcion!=caracteres:
    if descripcion>caracteres:
        print("Es mayor a 60 caracteres ingrese de nuevo")
        
        descripcion=str(input("Ingresar un breve resumen del artículo igual o menor a 60 caracteres: "))[:60]
print("")   


#utilizar variable upper para transformar a mayusculas el breve resumen 
mayu=descripcion.upper()

#printeamos longitud de caracteres
print("la longitud de caracteres del breve resumen es: ", caracteres)

#ultimos diez caracteres
diezcaracteres=descripcion[50:60]

#print de descripcion en mayusculas
print(mayu) 

#print diez caracteres
print(diezcaracteres)

