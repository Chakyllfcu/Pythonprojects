def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_int(msg)
    return tmp

print("Programa que acepte 3 números, indique en que posición (según el orden que se ingresan) están el mayor y el menor. Si hay un empate debe especificarlos.\n")

lista = []

for i in range(1,4):
    n = input_int(f"Inserte el numero {i}: ")
    lista.append(n)

if max(lista)==min(lista):
    print("\nHay un empate entre los numeros insertados")
else:
    print(f"El numero mayor de la lista es {max(lista)} que esta en la posicion {lista.index(max(lista))}\ny el menor es {min(lista)} que esta en la posicion {lista.index(min(lista))}")
