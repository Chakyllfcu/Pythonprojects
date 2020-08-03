from os import system
def input_str(msg):
    validacion = False
    while not validacion:
        a = input(msg)
        if len(a) >= 1 and a.isalpha() == True:
            validacion = True
        else:
            print('Debe insertar un dato valido.')
            a = input_str(msg)
        return a

def input_tel(msg):
    validacion = False
    while not validacion:
        a = input(msg)
        if len(a) >= 1 and a.isalnum() == True:
            validacion = True
        else:
            print('Debe insertar un dato valido.')
            a = input_tel(msg)
        return a


print("Aceptar nombre, apellido y teléfono de una persona. Crear en el disco un archivo html con los datos digitados.\n")
datos = {}

nombre=input_str("Ingrese un nombre: ")
apellido=input_str("Ingrese un apellido: ")
telefono=input_tel("Ingrese un telefono(8091234567): ")

datos[1]=nombre
datos[2]=apellido
datos[3]=telefono

archivo = open("dato.html",'r')
html = archivo.read()

html = html.replace('{nombre}',datos[1])
html = html.replace('{apellido}',datos[2])
html = html.replace('{telefono}',datos[3])
archivo.close()

nombre_archivo = nombre+'.html'
archivo = open(nombre_archivo,'w')
archivo.write(html)
archivo.close()

system("explorer "+nombre_archivo)

print("Revise su navegador predeterminado")




