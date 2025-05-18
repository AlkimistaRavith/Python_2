try:
    import sys
    import math

    if len(sys.argv) == 1:

        W = float(input("Ingrese su peso en Kiligramos: "))
        H = float(input("Ingrese su altura en Centímetros: "))

    elif len(sys.argv) == 3 :
        W = sys.argv[1]
        H = sys.argv[2]

        W = float(W)
        H = float(H)

    else :
        W = 0
        H = 1

    IMC = W / ( (H/100) ** 2)

    if IMC == 0 :
        print("Error en el ingreso. \nPuedes ingrersar <python imc.py>, o \n <python imc.py [peso en Kg] [altura en cm]")
    elif IMC < 18.5 :
        print(f"Su IMC es {IMC:.2f}. \nLa clasificación OMS es Bajo Peso")
    elif IMC >= 18.5 and IMC < 25 :
        print(f"Su IMC es {IMC:.2f}. \nLa clasificación OMS es Adecuado")
    elif IMC >= 25 and  IMC < 30 :
        print(f"Su IMC es {IMC:.2f}. \nLa clasificación OMS es Sobrepeso")
    elif IMC >= 30 and IMC < 35 :
        print(f"Su IMC es {IMC:.2f}. \nLa clasificación OMS es Obesidad Grado I")
    elif IMC >= 35 and IMC < 40 :
        print(f"Su IMC es {IMC:.2f}. \nLa clasificación OMS es Obesidad Grado II")
    else :
        print(f"Su IMC es {IMC:.2f}. \nLa clasificación OMS es Obesidad Grado III")

except ValueError:
    print("Error en el ingreso. \nPuedes ingrersar <python imc.py>, o \n <python imc.py [peso en Kg] [altura en cm]")