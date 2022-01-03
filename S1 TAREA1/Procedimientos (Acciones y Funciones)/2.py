# Construya una función “Eleva” Que reciba como parámetros una base y un
# exponente y retorne al algoritmo principal el resultado de elevar un numero al otro.

def elevar(base, exp):
    resultado = 1
    for i in range(exp):
        resultado *= base
    return resultado
        
print(5**4)