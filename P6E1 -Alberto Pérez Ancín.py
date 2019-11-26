#P6E1 Alberto Pérez Ancín
#Escribe un programa que te pida palabras y las guarde en una lista. Para terminar
#de introducir palabras, simplemente pulsa Enter. El programa termina escribiendo
#la lista de palabras.

lista = []
p = str("q")
while p != "":
    p = input("Escribe una palabra:\n")
    if p != "":
        lista.append(p)

print("Las palabras que has escrito son: ", lista)

