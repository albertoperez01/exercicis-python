#P7E2 Alberto Pérez Ancín
#Escribe un programa que lea el nombre y los dos apellidos de una persona
#(en tres cadenas de caracteres diferentes), los pase como parámetros a
#una función, y ésta debe unirlos y devolver una única cadena. La cadena
#final la imprimirá el programa por pantalla.

def f(n, a1, a2):
    p = n + " " + a1 + " " + a2 + " "
    return p

n = input("Escribe nombre: ")
a1 = input("Escribe primer apellido: ")
a2 = input("Escribe segundo apellido: ")
print(f(n, a1, a2))
    
    
