#P7E1 Alberto Pérez Ancín
#Escribe un programa que pida un texto por pantalla, este texto lo pase
#como parámetro a un procedimiento, y éste lo imprima primero todo en
#minúsculas y luego todo en mayúsculas.

def f(texto):
    print(texto.lower())
    print(texto.upper())

texto = input("Escribe un texto: ")
f(texto)
