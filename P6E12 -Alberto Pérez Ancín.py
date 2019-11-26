#P6E12 Alberto Pérez Ancín
#Escribir un programa para jugar a adivinar un número (el usuario piensa
#un número y el programa lo ha de adivinar). El programa empieza pidiendo
#entre qué números está el número a adivinar y luego intenta adivinar de
#qué número se trata. El usuario va diciendo si el número que ha dicho el
#programa es menor, mayor o igual al que se ha buscado.

import random
import time
intentos = []
random.seed(time.time())
minimo = int(input("Valor mínimo: "))
maximo = int(input("Valor máximo: "))
numero = str()

while minimo > maximo: 
    print(minimo, "Es mayor que", maximo, "vuelve a introducirlos")
    minimo = int(input("Valor mínimo:"))
    maximo = int(input("Valor máximo:"))
print("Piensa un numero entre", minimo, "y", maximo, "a ver si lo puedo adivinar")

while numero != "igual":
        adivinar = random.randint(minimo, maximo)
        print("Di si", adivinar, "es mayor, menor o igual al numero que has pensado")
        numero = str(input("Respuesta: "))
        if numero == "mayor":
            maximo = adivinar
        elif numero == "menor":
            minimo = adivinar
        elif numero == "igual":
            print("Gracias por jugar")
