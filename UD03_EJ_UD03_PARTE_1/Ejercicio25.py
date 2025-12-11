nombre = input("Introduce el nombre del postulante: ")
facultad = input("Introduce la facultad que va a estudiar (Ing.Sistemas, Derecho, Ing.Naviera, Ing.Pesquera, Contabilidad, Administracion): ")
match facultad.lower():
    case "ing.sistemas":
        importe = 350
        mensualidad = 650
    case "derecho":
        importe = 300
        mensualidad = 550
    case "ing.naviera":
        importe = 300
        mensualidad = 500
    case "ing.pesquera":
        importe = 310
        mensualidad = 460
    case "contabilidad":
        importe = 280
        mensualidad = 490
    case "administracion":
        importe = 360
        mensualidad = 520
    case _:
        print("Facultad no válida")
        importe = 0
        mensualidad = 0

igv = (importe + mensualidad) * 0.18
monto_final = importe + mensualidad + igv
print("Nombre del postulante:", nombre)
print("Facultad:", facultad)
print("Importe:", importe, "€")
print("Mensualidad:", mensualidad, "€")
print("IGV (18%):", igv, "€")
print("Monto final a pagar:", monto_final, "€")

