import requests
from json import loads
print("Tu horóscopo hoy es :\n")

tmp = requests.get("https://api.xor.cl/tyaas/")

datos = loads(tmp.text)

print("Fecha: "+datos['titulo'])
print("Nombre: "+datos['horoscopo']['escorpion']['nombre'])
print("Fecha de Signo: "+datos['horoscopo']['escorpion']['fechaSigno'])
print("Amor: "+datos['horoscopo']['escorpion']['amor'])
print("Salud: "+datos['horoscopo']['escorpion']['salud'])
print("Dinero: "+datos['horoscopo']['escorpion']['dinero'])
print("Color: "+datos['horoscopo']['escorpion']['color'])
print("Numero: "+datos['horoscopo']['escorpion']['numero'])


