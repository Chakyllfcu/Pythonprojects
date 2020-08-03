
print("Aceptar una palabra y determinar la cantidad de caracteres.\n")
validacion = False

while not validacion:
    a = input("Inserte una palabra: ")
    if len(a) >= 1 and a.isalpha() == True:
        validacion = True
        print(f"{a} tiene {len(a)} carácteres.")
    else:
        print('Debe insertar una palabra.')
