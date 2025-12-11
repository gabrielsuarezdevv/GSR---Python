# Extraer subcadenas usando slicing (rebanado de cadenas sin usar listas).

cadena = input("Introduce una cadena de texto: ")
inicio = int(input("Introduce el índice de inicio para el slicing: "))
fin = int(input("Introduce el índice de fin para el slicing: "))
subcadena = cadena[inicio:fin]
print("La subcadena extraída es:", subcadena)
