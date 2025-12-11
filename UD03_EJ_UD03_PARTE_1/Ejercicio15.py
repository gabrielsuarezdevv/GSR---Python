num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num3:
    menor = num3
else:
    menor = num2
        
if num2 >= num1 and num2 >= num3:
    mayor = num2
elif num1 >= num3:
    menor = num3
else:
    menor = num1
    
if num3 >= num1 and num3 >= num2:
    mayor = num3
elif num1 >= num2:
    menor = num2
else:
    menor = num1

print("El mayor es:", mayor)
print("El menor es:", menor)
if num1 == num2 == num3:
    print("Los tres números son iguales")
elif num1 == num2:
    print("El primer y segundo número son iguales")
elif num1 == num3:
    print("El primer y tercer número son iguales")
elif num2 == num3:
    print("El segundo y tercer número son iguales")