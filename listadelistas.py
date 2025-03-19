##esta es la seccion que llena el diccionario
"""
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
"""


##este es el codigo bueno
vendedores = {}
while True:
    nombre = input("Dame el nombre del vendedor (escribe 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    ventas = int(input("Ingresa los datos de las ventas: "))
    vendedores[nombre] = ventas  # Simplifiqué esto, no es necesario usar una tupla para un solo valor

# Segunda sección del código
mv = int(input("Dame una cantidad de marca de venta: "))

# Muestra solo los nombres de los vendedores cuyas ventas superan mv
lista = [nombre for nombre, ventas in vendedores.items() if ventas > mv]
print(lista)
