#P7E5 Alberto Pérez Ancín
#Escribe un programa que te pida una frase y una vocal, y pase estos datos
#como parámetro a una función que se encargará de cambiar todas las vocales
#de la frase por la vocal seleccionada. Devolverá la función la frase
#modificada, y el programa principal la imprimirá:

frase = input("Dime algo: ")
vocales = ["a", "e", "i", "o", "u"]
nada = ""


for i in frase:
    if i not in vocales:
        nada += i
    else:
        vocal = input("Dime una vocal: ")
        while vocal == i:
            vocal = input("Dime una vocal: ")
        else:
            nada += vocal

print(nada)
            
