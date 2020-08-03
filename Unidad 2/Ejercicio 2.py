def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_int(msg)
    return tmp
    
print("Inserte 2 números para calcular el promedio.")
n1 = input_int("Inserte primer numero: ")
n2 = input_int("Inserte segundo numero: ")
res = (n1 + n2)/2
print("El promedio es ", res)