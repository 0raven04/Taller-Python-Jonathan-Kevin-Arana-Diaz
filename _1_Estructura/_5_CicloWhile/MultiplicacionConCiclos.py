if __name__ == '__main__':

    x=int (input("Integra un numero: "))
    y=int(input("Ingresar el numero a mulltiplicar"))

    i:int=1;
    pot:int=0;

    while y>0:
        pot+=x
        y-=1
    print(pot)