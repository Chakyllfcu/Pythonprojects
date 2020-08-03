def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_int(msg)
    return tmp

print("Programa que acepte un numero, mostrar los números comprendidos desde 1 hasta el numero digitado.\n")
n = input_int("Inserte un numero: ")

for i in range(0,n):
    print(i+1)

input("\nPulse ENTER para salir del programa.")
