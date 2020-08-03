def input_float(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_float(msg)
    return tmp
    
print("Programa que acepte una temperatura en grados Celsius, mostrarla en grado farenheight y kelvin.")
T = input_float("Inserte la temperatura en C°: ")
F = (T * 1.8) + 32
K = T + 273.15
print("La temperatura en C° es :",T,"°")
print("La temperatura en F° es :",round(F,2),"°")
print("La temperatura en K° es :",round(K,2),"°")