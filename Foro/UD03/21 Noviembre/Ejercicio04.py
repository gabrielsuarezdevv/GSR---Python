# Construir manualmente una nueva cadena añadiendo un carácter a la vez (ejemplo: filtrar caracteres o construir cadenas invertidas).
nueva_cadena = ""
while True:
    cadena = input("Introduce una nueva letra de la cadena de texto: ")
    if cadena == "Fin":
        break
    else:
        for char in cadena:
            nueva_cadena += char
    
print("La nueva cadena construida es:", nueva_cadena)
