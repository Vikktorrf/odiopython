##esta es la seccion que llena el diccionario
vendedores= {}
while True:
    nombre= input("dame elnombre del vendedor (escribe salir para terminar): ")

    if nombre.lower() =='salir': 
        break
    
    ventas =int(input("ingresa los datos de las ventas: "))
    vendedores[nombre] = (ventas)
    
##es la segunda seccion del codigo    
mv = int(input("dame una cantidad de marca de venta: "))



##muestra todos los datos de los vendedores
lista = [[nombre,ventas] for nombre,ventas in vendedores.items() if (mv<ventas)]
print(lista)
