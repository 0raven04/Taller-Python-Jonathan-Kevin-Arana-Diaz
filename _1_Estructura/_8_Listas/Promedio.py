import statistics as mate
if __name__ == '__main__':
    numeros=[10,20,50,80,90,30,40]
    #opcion lenta
    """""
    conteo=0
    suma=0
    promedio=0
    for valor in numeros:
        suma+= valor
        conteo+=1

    promedio=suma/conteo
    print(promedio)
    """""

    #opcion medio lenta
    """""
    suma=0
    for valor in numeros:
        suma+=valor
    promedio=suma/len(numeros)
    print(promedio)
    """""

    #opcion rapida
    promedio = mate.mean(numeros)
    print(promedio)

    #añade un elemento al final de la lista
    mi_lista=[1,2,3]
    mi_lista.append(4)
    print(mi_lista)

    #
    mi_lista = [1, 2, 3]
    otra_lista = [4,5,6]
    mi_lista.extend(otra_lista)
    print(mi_lista)

    #inserta un elemento en una posicion especial
    mi_lista = [1,2,3]
    mi_lista.insert(1,4)
    print(mi_lista)

    #Elimina el primer elemento de la lista
    mi_lista = [1,2,3,2]
    mi_lista.remove(2 )
    print(mi_lista)

    #Elimina y devuelve el emelemento en una
    mi_lista = [1,2,3]
    elemento = mi_lista.pop(1)
    print(elemento)
    print(mi_lista)

    #Devuelve el indice de la primera aparicion de
    mi_lista = [1,2,3,2]
    indice = mi_lista.index(2)
    print(indice)

    #devuelve el número de veces que aparece un elemento en la lista
    mi_lista = [1,2,3,2]
    conteo = mi_lista.count(3)
    print(conteo)

    #Ordena los elementos de la lista de forma
    mi_lista = [3,1,4,2]
    mi_lista.sort()
    print(mi_lista)

    mi_lista.sort(reverse=True)
    print(mi_lista)

    #Iniverte el orden de los elementos de la lista
    mi_lista = [1,2,3,4]
    mi_lista.reverse()
    print(mi_lista)

    #Elimina todos los elementos de la lista.
    mi_lista = [1,2,3]
    mi_lista.clear()
    print(mi_lista)

    #Devuelve una copia superficial de la lista
    mi_lista = [1,2,3]
    mi_lista2=mi_lista
    copia_lista = mi_lista.copy()
    mi_lista.append(4)

    print(mi_lista2)

    #