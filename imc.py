#Esta validación es para solicitar solo numeros.
try:
    import sys
    import math

    #Este bloque es para determinar si se ingresa un argumento al ejecutar el programa, o si pide opción si no se ingresó argumento.
    if len(sys.argv) == 1:
        W = float(input("Ingrese su peso en Kiligramos: "))
        H = float(input("Ingrese su altura en Centímetros: "))

    elif len(sys.argv) == 3 :
        W = float(sys.argv[1])
        H = float(sys.argv[2])
    #Si no se ingresan la  cantidad de argumentos válidos se evalúa IMC = 0 (solo se agrega 1 argumento o sobre 2 argumentos)
    else :
        W = 0
        H = 1
    
    #Condicional para validar que el ingreso se realizó en Kg o cm.
    if W > 1000 or H < 5 :
        W = 1
        H = 1

    #Cálculo de IMC
    IMC = W / ( (H/100) ** 2)
    #Evaluación del IMC
    if IMC == 10000 :
        print("Has ingresado un valor no válido para tu peso o altura \n Recuerda ingresar tu peso en Kg y tu altura en cm.")
    elif IMC == 0 :
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
    print("Has ingresado datos que no son numéricos. \nPara calcular tu IMC, puedes ingrersar <python imc.py>, o \n <python imc.py [peso en Kg] [altura en cm]")