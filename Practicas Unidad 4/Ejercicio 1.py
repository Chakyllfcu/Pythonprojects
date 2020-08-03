def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_int(msg)
    return tmp

print("Programa que acepte 3 lados de un triangulo, indique si este es equilatero, Isósceles, Escaleno.")
a = input_int("Inserte el lado 1: ")
b = input_int("Inserte el lado 2: ")
c = input_int("Inserte el lado 3: ")

if a == b and a == c:
    print("El triangulo es equilatero")
else:
    if a == c or b == c:
        print("El triangulo es isosceles")
    else:
        print("El triangulo es escaleno")


