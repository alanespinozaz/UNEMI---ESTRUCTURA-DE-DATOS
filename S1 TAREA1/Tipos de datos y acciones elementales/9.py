#Dado un (1) número binario de cuatro (4) dígitos imprimir su bit da paridad.
#El bit de paridad es 1 si el número de bits 1 es impar y 0 en caso contrario.
bit1= int(input("Ingrese el primer número entre 0 y 1: "))
bit2= int(input("Ingrese el segundo número entre 0 y 1: "))
bit3= int(input("Ingrese el tercer número entre 0 y 1: "))
bit4= int(input("Ingrese el cuarto número entre 0 y 1: "))
resultado = bit1 + bit2 + bit3 + bit4
presentacion = str(bit1)+str(bit2)+str(bit3)+str(bit4)
if resultado % 2 == 0:
    print("El número de bits {} es par".format(presentacion))
else:
    print("El número de bits {} es impar".format(presentacion))
