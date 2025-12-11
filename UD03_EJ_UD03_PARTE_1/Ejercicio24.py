monto_compra = float(input("Introduce el monto de compra: "))
dia_semana = input("Introduce el día de la semana: ")
if dia_semana.lower() == "martes" or dia_semana.lower() == "jueves":
    descuento = monto_compra * 0.15
    total_a_pagar = monto_compra - descuento
    print("Descuento aplicado:", descuento, "€")
    print("Total a pagar:", total_a_pagar, "€")
else:
    print("No hay descuento aplicado")
    print("Total a pagar:", monto_compra, "€")