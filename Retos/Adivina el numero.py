import random
if __name__ == '__main__':
    numero_secreto = random.randint(1, 100)
    max_intentos = 10

    for intentos in range(1, max_intentos + 1):
        intento = input(f"Intento {intentos}/{max_intentos} - Adivina el número (entre 1 y 100): ")

        if intento.isdigit():
            intento = int(intento)

            if 1 <= intento <= 100:
                if intento < numero_secreto:
                    print("El número secreto es mayor. Intenta de nuevo.")
                elif intento > numero_secreto:
                    print("El número secreto es menor. Intenta de nuevo.")
                else:
                    print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
                    break
            else:
                print("Por favor, ingresa un número dentro del rango válido (1-100).")
        else:
            print("Entrada no válida. Por favor, ingresa un número entero.")
    else:
        print(f"Lo siento, has alcanzado el límite de intentos. El número secreto era {numero_secreto}.")
