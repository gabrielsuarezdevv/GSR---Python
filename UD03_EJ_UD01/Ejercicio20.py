numero = int(input("Ingrese un número entero: "))

if numero > 0:
    i = 1
    factorial = 1
    while i <= numero:
        factorial *= i
        i += 1
    print(f"El factorial de {numero} es {factorial}")
elif numero == 0:
    print("El factorial de 0 es 1")
else: 
    print("Introduce un número positivo.")