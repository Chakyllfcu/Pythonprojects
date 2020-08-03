a = input("Inserte una frase para indicar la cantidad de caracteres que contiene: \n\n")
cant = len(a) - a.count(' ')#len es para contar los caracteres, entonces uso count para contar los espacios en blanco y resto el resultado de ambos numeros para obtener la cantidad de caracteres sin espacios en blanco.
print("La frase tiene ",cant, " caracteres")