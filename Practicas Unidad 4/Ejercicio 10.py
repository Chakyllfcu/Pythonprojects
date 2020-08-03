from requests import get
from json import loads
from os import system
userlist = []
piclist = []

def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_int(msg)
    return tmp



print("Programa que solicite un numero luego mostrar en HTML el nombre, apellido y foto de cada persona. Indicar al final cuantas personas hay por genero.\n")

n = input_int("Inserte un numero: ")

urlx = f"https://randomuser.me/api/?results={n}"
datos = get(urlx)
objeto = loads(datos.text)

for i in range(0,n):
    nombre = objeto["results"][i]["name"]["first"]
    apellido = objeto["results"][i]["name"]["last"]
    genero = objeto["results"][i]["gender"]
    foto = objeto["results"][i]["picture"]["large"]
    userlist.append(f"<table class='table'><tr><th>Nombre:</th><td>{nombre}</td></tr><tr><th>Apellido:</th><td>{apellido}</td></tr><tr><th>Genero:</th><td>{genero}</td></tr></table>")
    piclist.append(foto)

archivo = open("dato.html",'r')
html = archivo.read()

#aqui eh que deberia ir mi logica del for 
#para que se agreguen nombres y apellidos pero nose jejeje xd
html = html.replace('{persona}',str(userlist)[1:-1])

nombre_archivo = 'Personas.html'
archivo = open(nombre_archivo,'w')
archivo.write(html)
archivo.close()

system("explorer "+nombre_archivo)

print("Revise su navegador predeterminado")
