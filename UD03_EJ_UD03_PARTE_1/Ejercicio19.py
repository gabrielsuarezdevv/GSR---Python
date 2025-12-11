saldo = 1000.0
print("Bienvenido a su Cajero Virtual")
print("1. Ingresar dinero en cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Salir")

opcion = input("Seleccione una opción (1, 2 o 3): ")
if opcion == "1":
    ingreso = float(input("Ingrese la cantidad a depositar: "))
    if ingreso > 0:
        saldo += ingreso
        print(f"Has ingresado {ingreso} dólares. Nuevo saldo: {saldo} dólares.")
    else:
        print("La cantidad a ingresar debe ser positiva.")
elif opcion == "2":
    retiro = float(input("Ingrese la cantidad a retirar: "))
    if 0 < retiro <= saldo:
        saldo -= retiro
        print(f"Has retirado {retiro} dólares. Nuevo saldo: {saldo} dólares.")
    else:
        print("Cantidad inválida o saldo insuficiente.")
elif opcion == "3":
    print("Gracias por usar el Cajero Virtual. ¡Hasta luego!")
else:
    print("Opción no válida.")
    