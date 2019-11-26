#P7E3 Alberto Pérez Ancín
#Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento, y éste debe mostrar la frase con un carácter en cada línea.

def f(frase):
    for i in range (len(frase)):
        print(frase[i])
     
frase = input("Escribe una frase: ")
f(frase)
    
