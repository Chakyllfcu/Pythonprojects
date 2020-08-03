from os import system

datos = []

def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite números")
        tmp = input_int(msg)
    return tmp

def input_str(msg):
    validacion = False
    while not validacion:
        a = input(msg)
        if len(a) >= 2 and a.isalpha() == True:
            validacion = True
        else:
            print('Debe insertar un dato valido.')
            a = input_str(msg)
        return a

def input_ced(msg):
    validacion = False
    while not validacion:
        a = input(msg)
        if len(a) == 11 and a.isnumeric() == True:
            validacion = True
        else:
            print('Debe insertar una cedula valida.')
            a = input_str(msg)
        return a

def Agregar():
    print("\nAgregar estudiante:\n")
    est = { }
    est['nombre'] = input_str("Digite el nombre: ")
    est['apellido'] = input_str("Digite el apellido: ")
    est['cedula'] = input_ced("Digite la Cedula(sin guiones): ")
    est['nota1'] = input_int("Digite la Nota 1: ")
    est['nota2'] = input_int("Digite la Nota 2: ")
    eq = (est['nota1'] + est['nota2']) / 2
    if eq >= 90:
        est['eq'] = 'A'
    elif eq >=80 and eq<=89:
        est['eq'] = 'B'
    elif eq >=70 and eq<=79:
        est['eq'] = 'C'
    elif eq >=60 and eq<=69:
        est['eq'] = 'D'
    else:
        est['eq'] = 'F'
    datos.append(est)
    print("\n¿Desea agregar un nuevo estudiante?\n1- Agregar otro estudiante\n2- Salir al Menu")
    opa = input("Digite una opcion: ")
    if opa == "1":
        Agregar()
    elif opa == "2":
        Menu()
    else:
        print("\nDebe digitar una opcion valida\n") 

def listado():
    if len(datos):
        print("\nNo hay estudiantes registrados\n")
        Menu()
    else:
        print("-------------------------------------")
        print("Estudiantes activos\n")
        n = 1
        for est in datos:
            print(f"{n}- {est['nombre']}\n{est['apellido']}\n{est['cedula']}\nNota 1:{est['nota1']}\nNota 2:{est['nota2']}\nEQ:{est['eq']}\n")
            n+=1


def Modificar():
    print("\nModificar estudiante\n")
    listado()
    ele = input_int("Digite el numero del estudiante que desea modificar o pulse 0 para volver atras: ")
    if ele == 0:
        Menu()
    else:
        est = datos[ele-1]
        ele2 = input("\n1- Nombre\n2- Apellido\n3- Cedula\n4- Notas\nQue dato del estudiante modificar: ")
        if ele2 == "1":
            est['nombre'] = input_str("Digite el nombre ")
            datos[ele-1] = est
        elif ele2 == "2":
            est['apellido'] = input_str("Digite el apellido ")
            datos[ele-1] = est
        elif ele2 == '3':
            est['cedula'] = input_ced("Digite la Cedula(sin guiones): ")
            datos[ele-1] = est
        elif ele2 == '4':
            est['nota1'] = input_int("Digite la Nota 1: ")
            est['nota2'] = input_int("Digite la Nota 2: ")
            eq = (est['nota1'] + est['nota2']) / 2
            if eq >= 90:
                est['eq'] = 'A'
            elif eq >=80 and eq<=89:
                est['eq'] = 'B'
            elif eq >=70 and eq<=79:
                est['eq'] = 'C'
            elif eq >=60 and eq<=69:
                est['eq'] = 'D'
            else:
                est['eq'] = 'F'
            datos[ele-1] = est
        else:
            print("\nDebe digitar una opcion valida\n") 
        
        print("\n¿Desea modificar otro estudiante?\n1- Modificar otro estudiante\n2- Salir al Menu")
        opa = input("Digite una opcion: ")
        if opa == "1":
            Modificar()
        elif opa == "2":
            Menu()
        else:
            print("\nDebe digitar una opcion valida\n") 

def Borrar():
    print("\nEliminar estudiante\n")
    listado()
    ele = input_int("Que estudiante desea borrar: ")
    est = datos[ele-1]
    del est['nombre']
    del est['apellido']
    del est['cedula']
    del est['nota1']
    del est['nota2']
    del est['eq']
    datos[ele-1] = est

def Exportar():
    print("\nExportar estudiante\n")
    listado()
    ele = input_int("Que estudiante desea exportar: ")
    est = datos[ele-1]

    archivo = open("dato.html",'r')
    html = archivo.read()
    
    html = html.replace('{nombre}',est['nombre'])
    html = html.replace('{apellido}',est['apellido'])
    html = html.replace('{cedula}',est['cedula'])
    html = html.replace('{nota1}',str(est['nota1']))
    html = html.replace('{nota2}',str(est['nota2']))
    html = html.replace('{eq}',est['nota2'])
    archivo.close()

    nombre_archivo = est['cedula']+'.html'
    archivo = open(nombre_archivo,'w')
    archivo.write(html)
    archivo.close()

    system("explorer "+nombre_archivo)

    print("Revise su navegador predeterminado\n")
    input("Presione Enter para volver al menu\n")

def ExportarTodos():
    print("\nExportar todos los estudiante\n")
    nombre_archivo = 'allstudents'+'.html'
    archivo = open(nombre_archivo,'w')
    html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Mis Datos</title>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
        </head>

        <body>
            <div class="container">
                <div class="txt-center">
                    <h3>Datos</h3>
    """
    archivo.write(html)
    archivo.close()
    for est in datos:
        html = f"""
                    <table class="table">
                            <tr>
                                <th>Nombre:</th>
                                <td>{est['nombre']}</td>
                            </tr>
                            <tr>
                                <th>Apellido:</th>
                                <td>{est['apellido']}</td>
                            </tr>
                            <tr>
                                <th>Cedula:</th>
                                <td>{est['cedula']}</td>
                            </tr>
                            <tr>
                                <th>Nota 1:</th>
                                <td>{est['nota1']}</td>
                            </tr>
                            <tr>
                                <th>Nota 2:</th>
                                <td>{est['nota2']}</td>
                            </tr>
                            <tr>
                                <th>Nota Literal:</th>
                                <td>{est['eq']}</td>
                            </tr>
                    </table>
            """
        archivo = open(nombre_archivo,'a')
        archivo.write(html)  
        archivo.close()

    html = f"""
                </div>
            </div>
        </body>
        </html>
    """
    archivo = open(nombre_archivo,'a')
    archivo.write(html) 
    archivo.close()

    system("explorer "+nombre_archivo)

    print("Revise su navegador predeterminado\n")
    input("Presione Enter para volver al menu\n")
            



print("Realiza un programita en python que permita registrar notas de estudiantes, para cada estudiantes solo se agregaran 2 notas")
def Menu():
    while True:
        print("Menú")
        print("1- Agregar\n2- Modificar\n3- Borrar\n4- Exportar un Estudiante\n5- Exportar Todos los estudiantes\n6- Salir del programa")
        opc = input("Digite una opcion: ")
        if opc == "1":
            Agregar()
        elif opc == "2":
            Modificar()
        elif opc == "3":
            Borrar()
        elif opc == "4":
            Exportar()  
        elif opc == "5":
            ExportarTodos()  
        elif opc == "6":
            print("Muchas gracias vuelva pronto")
            break
        else:
            print("Debe digitar una opcion valida") 
Menu()




 
