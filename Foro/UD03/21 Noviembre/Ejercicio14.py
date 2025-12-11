cadena = input("Introduce una cadena de texto: ")
contador_numeros = 0
for char in cadena:
    if char.isdigit():
        contador_numeros += 1
print("La cadena contiene", contador_numeros, "caracteres numéricos.")