#P6E9 Alberto Pérez Ancín
#Escribe un programa que te pida nombres de personas y sus números de teléfono. Para
#terminar debe pulsar “S” cuando te pida el nombre. El programa termina escribiendo
#nombres y números de teléfono. Nota: La lista en la que se guardan los nombres y
#números de teléfono tiene esta estructura[[nombre1, telef1], [nombre2, telef2],
#[nom3, telef3], etc], es decir, lista de listas.

usuario = []
usuarios = []
print("Introduce tu nombre de usuario: ")
nombre = str(input())
print("Introduce tu numero de telefono: ")
telefono = int(input())
while nombre != 's':
    usuario += [nombre, telefono]
    usuarios += [usuario]
    usuario = []
    print("Introduce tu nombre de usuario: ")
    nombre = str(input())
    print("Introduce tu numero de telefono: ")
    telefono = int(input())
for i in range (len(usuarios)):
    print(usuarios[i][0], end = ': ')
    print(usuarios[i][1])
