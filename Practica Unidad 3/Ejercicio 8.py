def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números enteros")
        tmp = input_int(msg)
    return tmp
print("Aceptar 2 números, determine el mayor.\n")
n1 = input_int("Inserte el primer numero: ")
n2 = input_int("Inserte el segundo numero: ")

tpl = (n1,n2)

print(f"{max(tpl)} es mayor que {min(tpl)}")
