import random

def juego_adivinanzas():
    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            # Pedir al usuario que ingrese un número
            adivinanza = int(input("Ingresa tu adivinanza: "))
            intentos += 1

            if adivinanza < numero_secreto:
                print("¡Muy bajo! Intenta nuevamente.")
            elif adivinanza > numero_secreto:
                print("¡Muy alto! Intenta nuevamente.")
            else:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Ejecutar el juego
juego_adivinanzas()

