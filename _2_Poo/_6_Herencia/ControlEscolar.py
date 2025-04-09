class listaDatos:
    def __init__(self, matricula: str, estudiante: str, asignatura: str):
        self.matricula = matricula
        self.estudiante = estudiante
        self.asignatura = asignatura


class controlEscolar:
    def __init__(self):
        self.lista = []

    def addEstudiante(self, matricula, estudiante, asignatura):
        self.lista.append(listaDatos(matricula, estudiante, asignatura))

    def show(self):
        for obj in self.lista:
            print(f"-----------------------\n Nombre: {obj.estudiante}\n Matrícula: {obj.matricula}\n Asignatura: {obj.asignatura}")


if __name__ == '__main__':
    escolar = controlEscolar()
    
    escolar.addEstudiante("12345678", "Paloma", "POO")
    escolar.addEstudiante("12345677", "Juan Carlos", "Matemáticas")
    escolar.addEstudiante("12345676", "Juan Carlos2", "Matemáticas2")
    escolar.addEstudiante("12345675", "Juan Carlos3", "Matemáticas3")
    escolar.addEstudiante("12345674", "Juan Carlos4", "Matemáticas4")

    escolar.show()
