def input_float(msg):
    tmp = 0
    try:
        tmp = float(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_float(msg)
    return tmp
print("Inserte un cateto y la hipotenusa para encontrar el cateto faltante")
a = input_float("Inserte la hipotenusa: ")
c = input_float("Inserte el cateto: ")
b = ((a**2) - (c**2))**(1.0/2) #Si pusiera 1/2 el resultado seria 0
print("El cateto faltante es ", round(abs(b),2))