def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_int(msg)
    return tmp
    
print("Inserte los valores de a,b & c para encontrar el valor de x1 y x2 segun la formula de ecuaciones de segundo grado.")
a = input_int("Inserte valor de a: ")
b = input_int("Inserte valor de b: ")
c = input_int("Inserte valor de c: ")
x1 = (-(b) + ((b**2-4*a*c)**(1.0/2)))/2*a
x2 = (-(b) - ((b**2-4*a*c)**(1.0/2)))/2*a
print("El valor de x1 es ", round(abs(x1)))
print("El valor de x2 es", round(x2))