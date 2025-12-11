# Reemplazar un carácter por otro recorriendo la cadena y concatenando a una nueva cadena.

cadena = input("Introduce una cadena de texto: ")
caracter_a_reemplazar = input("Introduce el carácter a reemplazar: ")
nueva_cadena = ""
for char in cadena:
    if char == caracter_a_reemplazar:
        caracter_nuevo = input("Introduce el nuevo carácter: ")
        nueva_cadena += caracter_nuevo
    else:
        nueva_cadena += char
print("La cadena modificada es:", nueva_cadena)