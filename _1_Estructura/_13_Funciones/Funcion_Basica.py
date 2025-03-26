import statistics as mate
def suma(a:int,b:int)->int:
    return a+b

def SumarArrglo(lista:list)->int:
    return sum(lista)

if __name__ == '__main__':

    print(f"La suma es {suma(5,10)}")
    lista = [1,2,3,4,5,6,7,8,9]
    print(f"La suma es {SumarArrglo(lista)}")