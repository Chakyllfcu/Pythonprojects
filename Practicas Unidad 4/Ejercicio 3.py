def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_int(msg)
    return tmp

print("Programa que acepte la medida de los cuatro lados de una figura: Determinar si esta es un cuadrado.\n")

a = input_int("Inserte el lado 1: ")
b = input_int("Inserte el lado 2: ")
c = input_int("Inserte el lado 3: ")
d = input_int("Inserte el lado 4: ")

if a == b and a == c and a == d:
    print("La figura es un cuadrado.")
else:
    print("La figura NO es un cuadrado.")

