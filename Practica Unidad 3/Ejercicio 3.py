from requests import get
from json import loads
print("Programa que acepte un RNC de RD mostrar el nombre de la empresa\n")
validacion = False

while not validacion:
    rnc = input("Inserte su RNC: ")
    if len(rnc) >= 1:
        validacion = True
        urlx = "https://api.adamix.net/apec/rnc/"+rnc
        datos = get(urlx)
        objeto = loads(datos.text)
        print("El nombre de la empresa es "+objeto['NOMBRE_COMERCIAL'])
    else:
        print('Debe insertar valores.')


