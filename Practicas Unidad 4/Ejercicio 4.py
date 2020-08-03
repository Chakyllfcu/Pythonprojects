def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_int(msg)
    return tmp

print("Programa que acepte un numero, mostrar en la consola la tabla de multiplicar\n")

n = input_int("Inserte un numero: ")

print(f"\nLa tabla de multiplicacion de {n}, es: \n")

for i in range(1,13):
    r = n * i
    print(f"{n} x {i} = {r}")
