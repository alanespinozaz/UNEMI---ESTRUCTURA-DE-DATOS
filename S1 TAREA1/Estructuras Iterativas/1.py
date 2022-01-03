# Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene
# dicho número.
def contar_caracteres(cadena):
    contador = 0
    
    while cadena [contador:]:
        contador += 1
    return contador

num = input("Ingrese un número entero N: ")
print("El número {}, tiene {} dígitos".format(num, len(num)))
