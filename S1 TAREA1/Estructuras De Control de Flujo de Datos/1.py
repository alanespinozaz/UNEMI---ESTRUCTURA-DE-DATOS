#Todos los años que se dividen exactamente entre 400, o que son divisibles
#exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos.
#Usando estas premisas crea un algoritmo que lea una fecha como un número
#entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si
#el mismo es un año bisiesto o no.
def bisiesto(fecha):
    if fecha % 400 ==0:
        return True
    elif fecha % 100 == 0:
        return False
    elif fecha % 4 == 0:
        return True
    else:
        return False
fecha = int(input("Ingrese la fecha en el siguiente orden ddmmaaaa: "))
print("¿La fecha {} es bisiesto?: {}".format(fecha, bisiesto(fecha)))
