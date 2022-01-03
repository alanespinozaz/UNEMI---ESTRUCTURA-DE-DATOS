import math
print("Dados tres números, Hacer una aplicación que calcule la resolvente.")
print("Hay que tener en cuanta la ecuación ax^2+bx+c")
print(" ")
print("................................................")
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
print(" ")
#Calculamos el discrimante
raiz= (b**2)-4*a*c
#comprobamos y calculamos
if raiz<0:
    print("...No existen soluciones reales...")
else:
    x1=(-b+math.sqrt(raiz))/(2*a)
    x2=(-b-math.sqrt(raiz))/(2*a)
    print(".....Soluciones.....")
    print("Solución de x1: ", "{:.2f}".format(x1))
    print("Solución de x2: ", "{:.2f}".format(x2))
