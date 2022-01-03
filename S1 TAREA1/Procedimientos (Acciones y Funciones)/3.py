# Escriba una función que calcule el perímetro del pentágono (siendo el perímetro la
# suma de los lados del polígono).

def perimet_pentagono(n,l):
    perm = n * l
    return perm

if __name__ == "__main__":
    n = 5
    l = int(input("Ingrese la longitud del poligono: "))
    result = perimet_pentagono(n,l)
    print("{}cm".format(result))