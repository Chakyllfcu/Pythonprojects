import math
print("Aceptar una cantidad de dinero, indicar cuantas veces se puede viajar en el metro con ese dinero usando tickets de viajero (35).")
a = input("Inserte cuanto dinero tiene: ")
res = int(a) / 35
r = math.floor(res)
print("Usted puede viajar en el metro",r,"veces con RD$",a,"pesos")

