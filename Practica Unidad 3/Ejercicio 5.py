import requests
from json import loads
import codecs
print("Programa que acepta una palabra en español y retornarla en balea\n")
validacion = False

while not validacion:
    palabra = input("Inserte una palabra: ")
    if len(palabra) >= 1:
        validacion = True
    else:
        print('Debe insertar datos.')

urlx = "https://diccionariobalear.com.es/api/?es="+palabra
datos = requests.get(urlx)
datos.encoding = 'utf-8-sig'
objeto = loads(datos.text)
print(f"La palabra en balea: {objeto[0]['balea']}")
