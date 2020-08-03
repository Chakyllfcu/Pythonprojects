def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_int(msg)
    return tmp

print("Programa que acepte 3 angulos de un triangulo: Rectángulo, Acutángulo u Obtusángulo.")

a = input_int("Inserte el lado a: ")
b = input_int("Inserte el lado b: ")
c = input_int("Inserte el lado c: ")


if a > b and a > c:
    if a**2 == (b**2) + (c**2):
        print("El triangulo es rectangulo.")
    elif a**2 > (b**2) + (c**2):
        print("El triangulo es obtusangulo")
    else:
        print("El triangulo es acutangulo")

elif b > a and b > c:
    if b**2 == (a**2) + (c**2):
        print("El triangulo es rectangulo.")
    elif b**2 > (a**2) + (c**2):
        print("El triangulo es obtusangulo")
    else:
        print("El triangulo es acutangulo")
else:
    if c**2 == (b**2) + (a**2):
        print("El triangulo es rectangulo.")
    elif c**2 > (b**2) + (a**2):
        print("El triangulo es obtusangulo")
    else:
        print("El triangulo es acutangulo")



