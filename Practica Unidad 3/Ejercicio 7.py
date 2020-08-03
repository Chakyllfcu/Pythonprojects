def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números enteros")
        tmp = input_int(msg)
    return tmp
print("Aceptar un numero y determinar si es par.\n")
n = input_int("Inserte un numero: ")

res = n%2

if res == 0:
    print(f"{n} es un numero par.")
else:
    print(f"{n} no es un numero par.")
