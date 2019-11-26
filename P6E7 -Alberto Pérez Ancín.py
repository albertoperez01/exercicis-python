#P6E7 Alberto Pérez Ancín
#Escribe un programa que pida un número (límite) y luego te pida números hasta que la
#suma de los números introducidos supere el límite inicial. El programa termina
#escribiendo la lista de números.

lista = []

l = int(input("Escribe límite: "))
v = int(input("Escribe un valor: "))
suma = v

while suma <= l:
    lista.append(v)
    v = int(input("Escribe un valor: "))
    suma = suma + v
    
lista.append(v)    

for i in range (len(lista)):
    if i == len(lista)-1:
        cadena = cadena + str(lista[i])
    else:
        cadena = cadena + str(lista[i])
    
print("El límite a superar es %d. La lista creada es ya que la suma de estos números es:",suma)
