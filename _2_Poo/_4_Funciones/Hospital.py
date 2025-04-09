class Hospital:
    def __init__(self):
        self.__NombrePaciente: str = ""
        self.__nss: int = 1258
        self.__enfermedad: str = ""

    # Métodos getters
    def getNombrePaciente(self) -> str:
        return self.__NombrePaciente

    def getNss(self) -> int:
        return self.__nss

    def getEnfermedad(self) -> str:
        return self.__enfermedad

    # Métodos setters
    def setNombrePaciente(self, nombre: str):
        self.__NombrePaciente = nombre

    def setNss(self, nss: int):
        self.__nss = nss

    def setEnfermedad(self, enfermedad: str):
        self.__enfermedad = enfermedad


if __name__ == '__main__':
    hospital = Hospital()

    # Usar métodos setters para asignar valores
    hospital.setNombrePaciente("Juan")
    hospital.setNss(16546898)
    hospital.setEnfermedad("Dolor de cabeza")

    # Usar métodos getters para obtener valores
    print(f"Nombre: {hospital.getNombrePaciente()}")
    print(f"NSS: {hospital.getNss()}")
    print(f"Enfermedad: {hospital.getEnfermedad()}")
