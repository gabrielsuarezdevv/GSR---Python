cadena1 = input("Introduce la primera cadena de texto: ")
cadena2 = input("Introduce la segunda cadena de texto: ")
cadena_concatenada = ""
for char in cadena1:
    cadena_concatenada += char
for char in cadena2:
    cadena_concatenada += char
print("La cadena concatenada es:", cadena_concatenada)