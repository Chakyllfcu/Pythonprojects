def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_int(msg)
    return tmp

print("Inserte los catetos para calcular la hipotenusa")
b = input_int("Inserte el cateto opuesto: ")
c = input_int("Inserte el cateto adyacente: ")
a = (b**2 + c**2)**(1.0/2) #Si pusiera 1/2 el resultado seria 0
print("La hipotenusa es ",round(a, 2))