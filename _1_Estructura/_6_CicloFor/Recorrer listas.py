if __name__ == '__main__':
    print("----------------------------------")
    lista=[1,2,"lunes",3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    #Una lista puede contener valores de diferente tipo
    #Ademas una lista es mutable

    #for elemento in lista:
    # print(elemento)

    lista.append(200)

    lista.append(400)
    lista.append("Sabado")
    lista.append(False)
    lista.append(2.69)
    lista.append(-100)

    lista2=[1200,1300,1500]

    lista.append(lista2)



    for elemento in lista:
        print(elemento)


    nombre:str
    nombre="luis"
    nombre.join("Gutierrez222222222")
    nombre +="Gutierrez1111111"
    print(nombre)

    lista3 = ["Federico", "pablo", "karla"]
    cadena:str=" - ".join(lista3)#La funcion join se utiliza para
    print(cadena)

    separado=cadena.split()
    for dato in separado:
        print(dato)
