#P6E4 Alberto Pérez Ancín
#Escribe un programa que te pida dos números, de manera que el segundo sea mayor que
#el primero. El programa termina escribiendo los dos números tal y como se pide:

lista = []

n = int(input("Escribe un número: "))
n2 = int(input("Escribe un número mayor: "))

while n <= n2:
    lista.append(n)
    n3 = int(input("Vuelve a introducir un número: "))
    if n3 > n:
        lista.append(n3)
        print("Las números que has escrito son: ", lista)
      



        
        
    
    
    
   
