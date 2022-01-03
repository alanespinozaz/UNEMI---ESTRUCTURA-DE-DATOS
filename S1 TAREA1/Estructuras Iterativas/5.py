# Dado un número entero N que representa una contraseña y asumiendo que una
# contraseña debe tener al menos 10 dígitos para ser segura, determine si la
# contraseña ingresada por el usuario es correcta, de no serlo debe pedirla
# nuevamente hasta que tenga los 10 (diez) dígitos solicitados y al ser correcta
# mostrar un mensaje de éxito al usuario, por salida estándar.

contr= input("Ingrese la contraseña: ")
if 10 <= len(contr) <= 16:
    print("Contraseña correcta")
else:
    print("La contraseña que ha ingresado es incorrecta.")

