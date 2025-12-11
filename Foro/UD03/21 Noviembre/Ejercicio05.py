# Verificar si un carácter específico está en la cadena con un ciclo y comparaciones.

cadena = input("Introduce una cadena de texto: ")
caracter = input("Introduce un carácter a buscar: ")
encontrado = False
for char in cadena:
    if char == caracter:
        encontrado = True
        break
if encontrado:
    print(f"El carácter '{caracter}' se encuentra en la cadena.")
else:
    print(f"El carácter '{caracter}' no se encuentra en la cadena.")