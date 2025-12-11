cadena = input("Introduce una cadena de texto: ")
contador_vocales = 0
vocales = "aeiouAEIOU"
for char in cadena:
    if char in vocales:
        contador_vocales += 1
print("La cadena contiene", contador_vocales, "vocales.")