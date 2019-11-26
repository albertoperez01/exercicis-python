#P7E4 Alberto Pérez Ancín
#Escribe un programa que pida una frase, y le pase como parámetro a una
#función dicha frase. La función debe sustituir todos los espacios en
#blanco de una frase por un asterisco, y devolver el resultado para que el
#programa principal la imprima por pantalla.

def f(frase):
    a = ""
    a = frase.replace(" ", "*")
    return a

frase= input("Escribe una frase: ")
print (f(frase))
