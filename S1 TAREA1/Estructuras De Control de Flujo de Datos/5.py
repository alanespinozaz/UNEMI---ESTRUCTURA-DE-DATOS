#Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es el
#mayor? y ¿cuál es el segundo mayor?
a = int(input("Ingrese en valor de A: "))
b = int(input("Ingrese en valor de B: "))
c = int(input("Ingrese en valor de C: "))
print(" ")
#Mayor
if b<a>c:
    print("El valor de A es el mayor")
elif a<b>c:
    print("El valor de B es el mayor")
elif a<c>b:
    print("El valor de C es el mayor")
else:
    print()
    
#Segundo Mayor
if b>a>c:
    print("El valor de A es segundo mayor")
elif a>b>c:
    print("El valor de B es segundo mayor")    
elif a>c>b:
    print("El valor de C es segundo mayor")
else: #Iguales
    if a==b and b==c and c==a:
        print("Los 3 valores son iguales")
    elif a==b and b!=c and a!=c:
        print("Los valores son A y B iguales")
    elif b==c and c!= a and b!=a :
        print("Los valores son B y C iguales")
    elif a == c and a!=b and c!=b:
        print("Los valores de A y C son iguales")
    else:
        print()
