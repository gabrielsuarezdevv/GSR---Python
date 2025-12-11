cadena = input("Introduce una cadena de texto: ")
opcion = input("¿Quieres convertir a mayúsculas o minúsculas? ")
nueva_cadena = ""
if opcion.lower() == "mayúsculas":
    nueva_cadena = cadena.upper()
elif opcion.lower() == "minúsculas":
    nueva_cadena = cadena.lower()
else:
    print("Opción no válida. La cadena permanecerá sin cambios.")
    nueva_cadena = cadena
print("La cadena modificada es:", nueva_cadena)
