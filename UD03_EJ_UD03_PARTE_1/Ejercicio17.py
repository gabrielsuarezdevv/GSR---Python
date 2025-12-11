usuario = input("Introduce el nombre de usuario: ")
contraseña = input("Introduce la contraseña: ")
if usuario == "admin" and contraseña == "1234":
    print("Inicio de sesión correcto")
else:
    print("Nombre de usuario o contraseña incorrecto")
