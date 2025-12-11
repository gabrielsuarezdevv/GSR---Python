cadena = input("Introduce una cadena de texto: ")
contador_mayusculas = 0
for char in cadena:
    if char.isupper():
        contador_mayusculas += 1
print("La cadena contiene", contador_mayusculas, "letras mayúsculas.")