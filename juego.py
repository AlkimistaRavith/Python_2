import sys

if len(sys.argv) > 2:
    print("python juego.py [tu nombre]")
else:
    nombre = sys.argv[1]
    print(f"hola {nombre}")