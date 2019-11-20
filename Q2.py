#2-a
def inverteMatriz(matriz):
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[1][0]
    d = matriz[1][1]

    detA = (a*d)-(b*c)

    if detA > 0:
        invDetA = (1/detA)
        aux = a
        matriz[0][0] = d
        matriz[1][1] = aux
        matriz[0][1] *= -1
        matriz[1][0] *= -1

        inva = invDetA * matriz[1][1]
        invb = invDetA * matriz[0][1]
        invc = invDetA * matriz[1][0]
        invd = invDetA * matriz[0][0]

        matriz[0][0] = invd
        matriz[0][1] = invb
        matriz[1][0] = invc
        matriz[1][1] = inva

        return matriz

    else:
        return None

#b 
def main():

    a = float(input("Entre com a: "))
    b = float(input("Entre com b: "))
    c = float(input("Entre com c: "))
    d = float(input("Entre com d: "))

    matriz = []
    for ind in range(2):
        matriz += [[0]*2]

    matrizOriginal = matriz
    matrizInvertida = inverteMatriz(matriz)

    imprimeMatriz(matrizOriginal)
    imprimeMatriz(matrizInvertida)

    def imprimeMatriz(matriz):

        for ind1 in range(len(matriz)):
            for ind2 in range(len(matriz[0])):
                print (matriz[ind1][ind2], end = "\t")
            print ()
