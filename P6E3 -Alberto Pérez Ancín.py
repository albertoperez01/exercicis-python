#P6E3 Alberto Pérez Ancín
#Escribe un programa que pida notas y los guarde en una lista. Para terminar de
#introducir notas, escribe una nota que no esté entre 0 y 10. El programa termina
#escribiendo la lista de notas.

lista = []
n = float(input("Escribe una nota:"))

while n <= 10 and n >= 0:
    lista.append(n)
    n = float(input("Escribe una nota:"))
       
print("Las notas que has escrito son:", lista)
