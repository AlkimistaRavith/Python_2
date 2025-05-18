
import random

opciones = ["caballero","dragon","hechicera"]
ganadas = 0
perdidas = 0
empates = 0

while True:
    jugador = input("Elige caballero, dragon o hechicera, (escribe salir para terminar el juego): ")
    jugador = jugador.lower()

    if jugador == "salir":
        print("Juego terminado")
        print(f"El resumen de la partida es: \n Victorias: {ganadas} \n Derrotas: {perdidas} \n Empates: {empates}")
        break
    if jugador not in opciones:
        print("Esta opción no es válida.")
        continue

    computador = random.choices(opciones)
    computador = computador[0]

    print(f"El computador a escogido: {computador}")

    if jugador == computador:
        print("Es un empate! La batalla continua...")
        empates += 1

    elif (jugador == "hechicera" and computador == "dragon") or \
         (jugador == "dragon" and computador == "caballero") or \
         (jugador == "caballero" and computador == "hechicera"):
         print("Has ganado la batalla!")
         ganadas += 1
    else:
        print("Has perdido, intentalo de nuevo!")
        perdidas += 1


""" 
import sys

if len(sys.argv) > 2:
    print("python juego.py [tu nombre]")
else:
 """