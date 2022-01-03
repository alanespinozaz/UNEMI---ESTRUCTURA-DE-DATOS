# Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la tabla
# del 1 hasta la del 10.

num = int(input("Digíte un número entero N: "))

for i in range(1, 11):
    print(f"{i} x {num} = {i * num}")
    
        