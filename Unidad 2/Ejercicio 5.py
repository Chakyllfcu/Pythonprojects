def input_float(msg):
    tmp = 0
    try:
        tmp = float(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_float(msg)
    return tmp
print("Inserte base y altura para calcular el area del triangulo.")
b = input_float("Inserte primer numero: ")
h = input_float("Inserte segundo numero: ")
a = (b * h)/2
print("El promedio es ", round(a,2))