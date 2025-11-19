numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
suma = numero1 + numero2
resta = numero1 - numero2
producto = numero1 * numero2
if numero2 != 0:
    division = numero1 / numero2
else:
    division = 0
print("Resultados de operaciones basicas:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Producto: {producto}")
print(f"División: {division}")