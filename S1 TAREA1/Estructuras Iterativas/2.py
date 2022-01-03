# Dado un número, determine si es capicúa.
# Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás. 
num = int(input("Ingrese un número: "))
dig1= num // 10000
dig2= (num//1000)%10
dig3= (num//100)%10
dig4= (num//10)%10
dig5= num%10
if dig1 == dig5 and dig2==dig4:
    print("Es Capicúa")
else:
    print("No es Capicúa")