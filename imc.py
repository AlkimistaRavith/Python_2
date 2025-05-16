import math

W = float(input("Ingrese su peso en Kiligramos: "))
H = float(input("Ingrese su altura en Centímetros: "))

IMC = W / ( (H/100) ** 2)

if IMC < 18.5:
    print(f"Su IMC es {IMC}, tienes una condición de Bajo Peso.")
if IMC < 18.5:
    print(f"Con un IMC de {IMC}, tienes una condición de Bajo Peso.")

print(f"tu IMC es: {IMC:.1f}")