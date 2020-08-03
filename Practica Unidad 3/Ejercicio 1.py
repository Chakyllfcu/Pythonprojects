def input_float(msg):
    tmp = 0
    try:
        tmp = float(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_float(msg)
    return tmp

print("Programa que acepte un salario, calcular el monto de la AFP correspondiente al mismo.\n")
s = input_float("Inserte su salario actual : RD$")
afp = input_float("Inserte deduccion actual del afp: %")
res = (s/100)*afp
print("El monto de la AFP correspondiente es de RD$",res)