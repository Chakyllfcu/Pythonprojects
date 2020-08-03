def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_int(msg)
    return tmp
    
print("Programa que acepte la cantidad de km por galón que da un vehículo de gasolina y la distancia. \nCalcular que cantidad de dinero se gastaría en un viaje digitado estos datos.\n\n")
c = input_int("Inserte cantidad km/g de su vehículo: ")
d = input_int("Inserte la distancia a recorrer: ")
p = input_int("Inserte el precio de la gasolina actual: ")
res = (c/d)*p
print("Usted gastaría RD$",res,"en el viaje.")

