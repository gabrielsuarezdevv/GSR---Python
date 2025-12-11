num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
if num2 != 0:
    division = num1 / num2
    print("La división de", num1, "entre", num2, "es:", division)
else:
    print("No se puede dividir entre cero.")

print("La suma de", num1, "y", num2, "es:", suma)
print("La resta de", num1, "y", num2, "es:", resta)
print("El producto de", num1, "y", num2, "es:", producto)