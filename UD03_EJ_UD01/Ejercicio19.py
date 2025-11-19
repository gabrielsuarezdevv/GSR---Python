numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

numeros = [numero1, numero2, numero3]

mayor = max(numeros)
menor = min(numeros)

print("El número mayor es:", mayor)
print("El número menor es:", menor)

if numero1 == numero2 == numero3:
    print("Los tres números son iguales.")
elif numero1 == numero2:
    print("El número 1 y 2 son iguales.")
elif numero1 == numero3:
    print("El número 1 y 3 son iguales.")
elif numero2 == numero3:
    print("El número 2 y 3 son iguales.")
