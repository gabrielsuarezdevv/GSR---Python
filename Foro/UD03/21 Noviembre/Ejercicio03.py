# Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador.

cadena = input("Introduce una cadena de texto: ")
caracter = input("Introduce un carácter a buscar: ")
contador = 0
for char in cadena:
    if char == caracter:
        contador += 1
print(f"El carácter '{caracter}' aparece {contador} veces en la cadena.")