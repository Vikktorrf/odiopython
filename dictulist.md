"""
programa que solicite el nombre de un equiopo de futbol
juegos ganados perdidos y empatados
ejemplo del diccionario
('chivas':(13,4,3))
porcentaje de juegos ganados
lista con los juegos ganados de cada equipo
"""

 ##juegos ganados
 # Inicializamos un diccionario vacío para almacenar los equipos
equipos = {}

while True:
    nombre = input("Ingrese el nombre del equipo (o 'salir' para terminar): ")
    
    if nombre.lower() == 'salir':
        break
    
    while True:
        try:
            jg = int(input("Ingrese partidos ganados: "))
            jp = int(input("Ingrese partidos perdidos: "))
            je = int(input("Ingrese partidos empatados: "))
            
            if jg < 0 or jp < 0 or je < 0:
                print("Error: Los valores no pueden ser negativos")
                continue
                
            partidos = jg + jp + je
            
            if partidos > 20:
                print(f"Error: El total de partidos ({partidos}) excede el máximo permitido de 20")
                break
                
            equipos[nombre] = (jg, jp, je)
            break
            
        except ValueError:
            print("Error: Por favor ingrese solo números enteros")

print("\nDatos de los equipos:")
print(equipos)

# Nueva sección para mostrar equipos y juegos ganados
print("\nLista de equipos y partidos ganados:")
for equipo, datos in equipos.items():
    ##solo me faltaria conseguir el porcentaje de los valores que se ganaron, pero ess lo consigo despues
    print(f"Equipo: {equipo} - Partidos ganados: {datos[0]}")

##esta es la solucion completa del problema, aunque tengo que estudiam labmda

"""
equipos = {}

while True:
    nombre = input("Ingrese el nombre del equipo (o 'salir' para terminar): ")

    if nombre.lower() == 'salir':
        break

    while True:
        try:
            jg = int(input("Ingrese partidos ganados: "))
            jp = int(input("Ingrese partidos perdidos: "))
            je = int(input("Ingrese partidos empatados: "))

            if jg < 0 or jp < 0 or je < 0:
                print("Error: Los valores no pueden ser negativos")
                continue

            partidos = jg + jp + je

            if partidos > 20:
                print(f"Error: El total de partidos ({partidos}) excede el máximo permitido de 20")
                continue # Regresa al inicio del bucle interno para reingresar los datos

            equipos[nombre] = (jg, jp, je)
            break # Sale del bucle interno si los datos son válidos

        except ValueError:
            print("Error: Por favor ingrese solo números enteros")

print("\nDatos de los equipos:")
print(equipos)

print("\nLista de equipos y partidos ganados:")
lista_ganados = [] # Inicializamos la lista para almacenar los partidos ganados

for equipo, datos in equipos.items():
    ganados = datos[0]
    total_partidos = sum(datos)  # Calcula el total de partidos
    porcentaje_ganados = (ganados / total_partidos) * 100 if total_partidos > 0 else 0  # Evita división por cero

    print(f"Equipo: {equipo} - Partidos ganados: {ganados} - Porcentaje de partidos ganados: {porcentaje_ganados:.2f}%")

    lista_ganados.append((equipo, ganados)) # Agregamos el equipo y sus partidos ganados a la lista

print("\nLista de equipos y partidos ganados (lista_ganados):")
print(lista_ganados)

# Opcional:  Ordenar la lista por partidos ganados (de mayor a menor)
lista_ganados.sort(key=lambda item: item[1], reverse=True) #sort por el segundo elemento de cada tuple
print("\nLista ordenada por partidos ganados (de mayor a menor):")
print(lista_ganados)
"""


## ESTA ES LA VERSION FINAL QUE CREO QUE CONTIENE TODO
```python
equipos = {}
while True:
    nombre = input("Ingrese el nombre del equipo (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    while True:
        try:
            jg = int(input("Ingrese partidos ganados: "))
            jp = int(input("Ingrese partidos perdidos: "))
            je = int(input("Ingrese partidos empatados: "))
            if jg < 0 or jp < 0 or je < 0:
                print("Error: Los valores no pueden ser negativos")
                continue
            partidos = jg + jp + je
            if partidos > 20:
                print(f"Error: El total de partidos ({partidos}) excede el máximo permitido de 20")
                continue
            equipos[nombre] = (jg, jp, je)
            break
        except ValueError:
            print("Error: Por favor ingrese solo números enteros")

print("\nDatos de los equipos:")
print(equipos)

print("\nLista de equipos y partidos ganados:")
lista_ganados = []
for equipo, datos in equipos.items():
    ganados = datos[0]  # Partidos ganados
    perdidos = datos[1]  # Partidos perdidos
    total_partidos = sum(datos)
    # Calculamos el porcentaje de partidos ganados
    if total_partidos > 0:
        porcentaje_ganados = (ganados / total_partidos) * 100
        porcentaje_perdidos = (perdidos / total_partidos) * 100
    else:
        porcentaje_ganados = 0
        porcentaje_perdidos = 0
    print(f"Equipo: {equipo} - Partidos ganados: {ganados} - Porcentaje de partidos ganados: {porcentaje_ganados:.2f}% - Porcentaje de partidos perdidos: {porcentaje_perdidos:.2f}%")
    lista_ganados.append((equipo, ganados))
 ##si no les deja usar esto usen burbuja 
    lista_ganados.sort()

print("\nLista de equipos y partidos ganados (lista_ganados):")
print(lista_ganados)
```
