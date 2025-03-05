if __name__ == '__main__':
    a=input("Escribe un nombre")
    b=input("Escribe un segundo nombre")

    c=len(a)
    d=len(b)

    if c>d:
       print(f"El nombre mas largo es {a}")
    elif c==d:
        print("Los nombres son igual de largos")
    else:
            print(f"El nombre mas largo es {b}")