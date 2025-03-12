if __name__ == '__main__':
    lista = [16,8,1,4,5,1,5,1,6,8,7,1,2,3,3,5,6,7,98,9]
    totales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    adoptados: int = 0
    for elemento in lista:

        match elemento:
            case 1:
                totales[0] +=1
            case 2:
                totales[1] += 1
            case 3:
                totales[2] += 1
            case 4:
                totales[3] += 1
            case 5:
                totales[4] += 1
            case 6:
                totales[5] += 1
            case 7:
                totales[6] += 1
            case 8:
                totales[7] += 1
            case 9:
                totales[8] += 1
            case 10:
                totales[9] += 1
            case _:
                adoptados += 1
    i:int=0
    for elemento in totales:
        i+=1
        print(f"{i}.-{elemento}")
    else:
       print(f"no validos  {adoptados}")

