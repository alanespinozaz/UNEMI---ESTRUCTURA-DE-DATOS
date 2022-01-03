import math
#Dados dos (2) lados de un triángulo en cm,
#calcular la hipotenusa del mismo.
cat1 = float(input("Ingrese el primer cateto: ")) 
cat2 = float(input("Ingrese el segundo cateto: "))
hipt = math.sqrt(cat1**2 + cat2**2)
print("La hipotenusa es: ", hipt)