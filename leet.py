"""
A este ya le entendi un poquito mas, mi unica complicacion fue al momento de mapear, ya que era conciente de que el String lo tenia que pasar a char y luego a String otra vez para que 
pudiera traducir y tomar el valor de cada letra del diccionario, sin embargo con ayuda de la inteligencia artifical logre entender un poco mas como servia esto de python
y sus variables todas raras que nomas no me acostumbro, tambien vi como es que funcionaba traduct.get(i,i) que basicamente es la parte que toma el valor del diccionario y lo 
cambia, el for fue simplemente para poder escribirlo, la primera vez salio mal ya que solo habia llamado a la funcion para traducir hasta que cree letterT y de ahi ya sirvio




 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""

##para esto primero que nada es obvio que tengo que usar un mapa, el caso es que no recuerdo bn la sintaxis en python

traduct = {
    "a":"4",
    "b":"I3",
    "c":"[",
    "d":")",
    "e":"3",
    "f":"|=",
    "g":"&",
    "h":"#",
    "i":"1",
    "j":"_|",
    "k":">|",
    "l":"1",
    "m":"//\\\\",
    "n":"^/",
    "o":"0",
    "p":"|*",
    "q":"(_,)",
    "r":"|2",
    "s":"5",
    "t":"7",
    "u":"(_)",
    "v":"\/",
    "w":"\/\/",
    "x":"><",
    "y":"j",
    "z":"2"
    }
word = input("escribe lo que quieres traducir a leet").lower()
##me di cuenta que si queria que sirviera tenia que dividir mi String en Chat
result=""
for letra in word:
    letterT = traduct.get(letra,letra)
    result = result + letterT
print(result)
##ahora aqui va la funcion de traducir lo que puse en mi dicciona
