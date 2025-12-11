cadena = input("Introduce una cadena de texto: ")
contador_caracteres = {}
for char in cadena:
    if char in contador_caracteres:
        contador_caracteres[char] += 1
    else:
        contador_caracteres[char] = 1
nueva_cadena = ""
for char in cadena:
    if contador_caracteres[char] > 1 and char not in nueva_cadena:
        nueva_cadena += char
print("La nueva cadena es:", nueva_cadena)
