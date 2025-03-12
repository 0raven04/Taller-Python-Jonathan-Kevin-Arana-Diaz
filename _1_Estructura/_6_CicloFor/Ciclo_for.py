import sys

if __name__ == '__main__':
    print("Rango de 0 a 9 ")
    for i in range(10):
        print(f"{i}")
    print("Rango de 6 a 11 ")
    for i in range(6,12):
        print(f"{i}")
    print("Rango de 6 a 11 con incrementos de 3 en 3 ")
    for i in range(6, 13 ,3):
        print(f"{i}")
    print("----------------------------------")
    for i in range(1,20):
        print(f"{i}", end="")

        sys.stdout.write("Texto son salto de liena")