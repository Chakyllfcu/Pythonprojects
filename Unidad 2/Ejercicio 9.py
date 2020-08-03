import math
print("Para hacer una hamburguesa se necesita 1 pan, 2 carnes, 1/5 de libra de tocineta. Calcule cuantas haburguesas se pueden hacer segun la cantidad de estas materias primas que existen en un almacén.")
p = input("Inserte el numero de panes en almacen: ")
c = input("Inserte el numero de carnes en almacen: ")
t = input("Inserte las libras de tocinetas en almacen: ")
hp = int(p)
hc = int(c)/2
ht = int(t)/0.2
h=[hp,hc,ht]
print("Se pueden hacer",math.floor(min(h)),"hamburguesas.")