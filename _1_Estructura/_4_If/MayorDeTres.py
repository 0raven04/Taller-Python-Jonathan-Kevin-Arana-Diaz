if __name__ == '__main__':
    a=int(input("Proporciona un numero: "))
    b=int(input("Proporciona segundo numero: "))
    c=int(input("Proporciona tercer numero: "))

    if a>b:
        if a>c:
            print(f"El mayor es {a}")
        else:
            print(f"El mayor es {b}")
    else:
        if b>c:
            print(f"El mayor es {b}")
        else:
            print(f"El mayor es {c}")
