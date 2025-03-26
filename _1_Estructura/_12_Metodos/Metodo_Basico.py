import statistics as mate
def suma(a: int, b=None , c=None):
    if b is None:
        print(f"{a}")
    elif c is None:
        print(f"La suma de {a} + {b} es {a + b}")
    else:
        print(f"La suma de {a} + {b} + {c} es {a + b + c}")

def promedioArreglo(lista):
    lista.append(5)
    lista.append(45)
    lista.append(56)
    p=mate.mean(lista)
    print(f"El promeio es {p}")

if __name__ == '__main__':
    suma(10)
    suma(12)
    suma(154)

    suma(10, 52)
    suma(24, 47)
    suma(12, 255)

    suma(12, 255, 10)
    suma(33, 100, 102)
    suma(54, 225, 102)

    lista2=[1,2,3,4,5]
    promedioArreglo(lista2)
    print(lista2)

    #La lista saldra de la lista alterada