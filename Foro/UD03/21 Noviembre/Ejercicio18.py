cadena = input("Introduce una cadena de texto: ")
nueva_cadena = ""
vocales = "aeiouAEIOU"
for char in cadena:
    if char not in vocales:
        nueva_cadena += char
print("La nueva cadena es:", nueva_cadena)
