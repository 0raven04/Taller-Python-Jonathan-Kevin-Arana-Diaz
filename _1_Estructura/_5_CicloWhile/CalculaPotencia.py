if __name__ == '__main__':
    x=int (input("Integra un numero: "))
    y=int(input("Ingresar la potencia"))

    i:int=1;
    pot:int=1;

    while i<=y:
        pot=pot*x
        i=i+1;
    print(f"El resultado de {x}^{y}={pot}")
