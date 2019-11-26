#P6E2 Alberto Pérez Ancín
#Escribe un programa que te pida números y los guarde en una lista. Para terminar de
#introducir número, simplemente escribe “Salir”. El programa termina escribiendo la
#lista de números.

lista = []
n = str("P")

while n != "Salir":
    n = input("Escribe un número:")
    if n != "Salir":
        lista.append(n)
                      
print("Los números que has escrito són:", lista)
        
