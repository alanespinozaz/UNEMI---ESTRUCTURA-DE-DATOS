# Dado un número N determinar si es un número primo.
# Nota: Un número primo es aquel que solo es divisible por 1(uno) y por el mismo. 

def es_primo(num):
    contador = 0
    for i in range (1, num+1):
        if num % i ==0:
            contador += 1
    
    if contador == 2:
        print("Es un número primo.")
        return True
    else:
        print("Es un número primo.")
        return False
    
num = int(input("Ingrese un número N: "))    
print(es_primo(num))
