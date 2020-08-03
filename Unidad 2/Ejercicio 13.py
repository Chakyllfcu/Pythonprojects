from datetime import date
print("Programa que acepte la fecha de nacimiento de una persona. Determine la edad de la misma.")

nacimiento = input("Inserte su fecha en el siguiente formato aaaa/mm/dd: ")

y = int(nacimiento[0:4])
m = int(nacimiento[5:7])
d = int(nacimiento[8:10])
fecha = date(y,m,d)

print("Fecha actual es ",date.today())
print("Fecha de nacimiento es ",fecha)

edad = int(abs(date.today()-fecha).days/365.25)

print("La edad de usted es ",edad)