#P6E5 Alberto Pérez Ancín
#Escribe un programa que te pida números cada vez más grandes y que se guarden en una
#lista. Para acabar de escribir los números, escribe un número que no sea mayor que
#el anterior. El programa termina escribiendo la lista de números:

print("Introduce un numero")
numeros = []
numero = int(input())
numeros.append(numero)
print("Introduce un numero mayor que", numero)
numero = int(input())
numeros.append(numero)

while numeros[-2] < numeros[-1]:
    print('introduce un numero mayor que', numero)
    numero = int(input())
    numeros.append(numero)
print("Los numeros son:", end = '')

del numeros[-1]
for i in range(len(numeros)):
    if i == (len(numeros)-1):
        print(numeros[i], end='')
    if i != (len(numeros)-1):
        print(numeros[i], ',', end = '')
    
    
    

