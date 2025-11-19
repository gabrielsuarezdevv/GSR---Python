precioVenta = float(input("Introduce el precio de venta del producto: "))
precioReal = float(input("Introduce el precio real del producto: "))
porcentajeDescuento = ((precioVenta - precioReal) / precioVenta) * 100
print(f"El porcentaje de descuento aplicado es: {porcentajeDescuento}%")
