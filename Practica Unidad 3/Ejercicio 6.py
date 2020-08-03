def input_float(msg):
    tmp = 0
    try:
        tmp = float(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_float(msg)
    return tmp
print("Aceptar la distancia y el tiempo recorrido, calcular la velocidad promedio a que se viajaba.\n")

d = input_float("Inserte la distancia(km): ")
t = input_float("Inserte el tiempo recorrido(horas): ")

res = (d/t)

print(f"La velocidad promedio fue de {round(res,2)} km/h")