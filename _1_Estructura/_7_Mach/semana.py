import sys

if __name__ == '__main__':
    sys.stdout.write("proporciona un número del dia de la semana")
    num=int(input())
    semana=""
    match num:
        case 1:semana="Lunes"
        case 2:semana="Martes"
        case 3:semana="Miercoles"
        case 4:semana="Jueves"
        case 5:semana="Viernes"
        case 6:semana="Sábado"
        case 7:semana="Domingo"
        case _:semana="Numero no valido"
    if num >=1 and num<=7:
        sys.stdout.write(f"El dia de la semana indicado es {semana}")
    else:
        sys.stdout.write(f"{semana}")