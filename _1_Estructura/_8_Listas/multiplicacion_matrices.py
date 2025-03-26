
if __name__ == '__main__':
    #A=[1,2,3]
    # =[4,5,6]

    #B=[-1,0]
    #  [0,1]
    #  [1,1]

    matrizA=[[1,2,3],
             [4,5,6]]

    matrizb=[[-1,0],
             [0,1],
             [1,1]]
    res = [[0,0],
           [0,0]]
    tamA=len(matrizA)
    tamB=len(matrizb)

    print(f"El tamaño de la matriz A es {tamA}")
    print(f"El tamaño de la matriz B es {tamB}")


    for i in range(len(matrizA)):
        for j in range(len(matrizb[0])):
            for k in range(len(matrizb)):
                res[i][j]+=matrizA[i][k] * matrizb[k][j]
    print(f"El resultado es {res}")