def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_int(msg)
    return tmp


print("Programa que permita saber si un ano es bisiesto: debe ser divisible por 4, no debe ser visible por 100, excepto que tambien sea divisible por 400\n")

n = input_int("Inserte un año: ")

if n%4 == 0:
    if n%100 == 0:
        print(f"El año {n} no es bisiesto.")
    else:
        print(f"El año {n} es bisiesto.")
else:
    print(f"El año {n} no es bisiesto.")
