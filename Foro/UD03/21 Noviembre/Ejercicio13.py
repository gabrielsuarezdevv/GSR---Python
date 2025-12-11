cadena = input("Introduce una cadena de texto: ")
cadena_sin_espacios = ""
for char in cadena:
    if char != " ":
        cadena_sin_espacios += char
print("La cadena sin espacios es:", cadena_sin_espacios)