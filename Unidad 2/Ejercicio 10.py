import math
print("Programa que acepte una cantidad de dinero en pesos. Calcule cuanto es ese monto en dolares")
a = input("Inserte el valor en pesos dominicanos: RD$")
dol = int(a) / 58
print("El valor en dolares es US$",round(dol,2))