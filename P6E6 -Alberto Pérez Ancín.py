#P6E6 Alberto Pérez Ancín
#Escribe un programa que pida primero dos números (máximo y mínimo) y que después te
#pida números intermedios. Para terminar de escribir números, escribe un número que
#no esté comprendido entre los dos valores iniciales. El programa termina escribiendo
#la lista de números.
lista = []

n1= int(input("Escribe un número: "))
n2= int(input("Escribe un número mayor que %d:\n" % (n1)))


while n2 < n1:
    lista.append(n1)
    n2 = int(input("%d no es mayor que %d. Vuelve a probar:\n" % (n2, n1)))


n3 = int(input("Escribe un número entre %d y %d:" % (n1, n2)))

while n3 > n1:
    lista.append(n3)
    n3 = int(input("Escribe un número entre %d y %d:" % (n1, n2)))
    if n2 < n3:
      print("Los números situados entre %d y %d que has escrito son:" % (n1, n2), lista)
      
print("Los números situados entre %d y %d que has escrito son:" % (n1, n2), lista)
    

