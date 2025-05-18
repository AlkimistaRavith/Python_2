
import random
import sys

opciones = ["piedra","papel","tijeras"]

#Este bloque es para determinar si se ingresa un argumento al ejecutar el programa, o si pide opción si no se ingresó argumento.
if len(sys.argv) == 2 :
    jugador = sys.argv[1]
    jugador = jugador.lower()

elif len(sys.argv) == 1 : 
    jugador = input("Escoge tu opción: piedra, papel o tijeras: ")
    jugador = jugador.lower()
else :
    print("Esta opción no es válida. \n Puedes escribir <python juego.py>, o \n <python juego.py [piedra, papel o tijeras]>")

#Bloque para determinar si la opción es válida o si se ejecuta el juego (escoge el PC)
if jugador not in opciones:
    print("Esta opción no es válida. \n Puedes escribir <python juego.py>, o \n <python juego.py [piedra, papel o tijeras]>")
else :
    computador = random.choices(opciones)
    computador = computador[0]

    print(f"Tu jugaste {jugador}")
    print(f"El computador jugó {computador}")
    #Bloque dentro del bloque de validación, para ejecutar el juego y determianr ganador, perdedor o empate
    if jugador == computador:
        print("Es un empate!")

    elif (jugador == "piedra" and computador == "tijeras") or \
            (jugador == "tijeras" and computador == "papel") or \
            (jugador == "papel" and computador == "piedra"):
            print("Ganaste!")

    else:
        print("Has perdido, intentalo de nuevo!")