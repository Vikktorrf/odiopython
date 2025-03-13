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
