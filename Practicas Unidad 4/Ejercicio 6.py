def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_int(msg)
    return tmp

print("Programa que acepte un numero, mostrar los números comprendidos desde el hasta el 1 de manera descendente.\n")
n = input_int("Inserte un numero: ")

for n in range(n,0,-1):
    print(n)



