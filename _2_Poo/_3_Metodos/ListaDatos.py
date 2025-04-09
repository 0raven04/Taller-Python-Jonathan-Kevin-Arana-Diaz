class listaDatos:
    def __init__(self,matricula:str, estudiante:str, asignatura:str):
        self.matricula=matricula
        self.estudiante=estudiante
        self.asignatura=asignatura
if __name__ == '__main__':
    lista=[]

    lista.append(listaDatos("12345678", "Juan Carlos", "matematicas"))
    lista.append(listaDatos("12345677", "Juan Carlos2", "matematicas2"))
    lista.append(listaDatos("12345676", "Juan Carlos3", "matematicas3"))
    lista.append(listaDatos("12345675", "Juan Carlos4", "matematicas4"))

    for obj in lista:
        print(f"----------------------- \n nombre: {obj.estudiante}\n matricula {obj.matricula}\n asiganatura {obj.asignatura}")