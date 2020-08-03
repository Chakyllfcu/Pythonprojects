from requests import get
from os import system

class empleado:
    cedula = '-'
    salario = 0.0
    cargo = 'n/a'
    nombre = 'n/a'
    apellido = 'n/a'

    def __init__(self,cedula, salario, cargo, nombre = "",apellido = ""):
        self.cedula = cedula
        self.salario = salario
        self.cargo = cargo
        self.nombre = nombre
        self.apellido = apellido
        if len(nombre) == 0:
            self.cargar_datos()

    def cargar_datos(self):
        url = "https://api.adamix.net/apec/cedula/"+self.cedula
        datos = get(url).json()
        if datos['ok']:
            self.nombre = datos['Nombres']
            self.apellido = datos['Apellido1'] +' '+datos['Apellido2']
        else:
            self.nombre("Cedula no valida")

    
class nomina:
    empleados = []
    def Agregar(self,emp):
        self.empleados.append(emp)

    def Mostrar(self):
        if len(self.empleados) == 0:
            print("No hay empleados registrados")
        
        else:
            n=1
            for emp in self.empleados:
                print(f"\n{n}- {emp.nombre}\n{emp.apellido}\n{emp.cedula}\n{emp.salario}\n{emp.cargo}\n")
                n+=1

    def Exportar(self,ele):
        emp = self.empleados[int(ele)-1]
        archivo = open("dato.html",'r')
        html = archivo.read()
        html = html.replace('{nombre}',emp.nombre)
        html = html.replace('{apellido}',emp.apellido)
        html = html.replace('{cedula}',emp.cedula)
        html = html.replace('{salario}',emp.salario)
        html = html.replace('{cargo}',emp.cargo)
        archivo.close()

        nombre_archivo = emp.cedula+'.html'
        archivo = open(nombre_archivo,'w')
        archivo.write(html)
        archivo.close()

        system("explorer "+nombre_archivo)

        print("Revise su navegador predeterminado\n")
        input("Presione Enter para volver al menu\n")
    
    def Exportar_Todos(self):
        print("\nExportar todos los empleados\n")
        nombre_archivo = 'allemployees'+'.html'
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
        for emp in self.empleados:
            html = f"""
                    <table class="table">
                            <tr>
                                <th>Nombre:</th>
                                <td>{emp.nombre}</td>
                            </tr>
                            <tr>
                                <th>Apellido:</th>
                                <td>{emp.apellido}</td>
                            </tr>
                            <tr>
                                <th>Cedula:</th>
                                <td>{emp.cedula}</td>
                            </tr>
                            <tr>
                                <th>Sueldo:</th>
                                <td>{emp.salario}</td>
                            </tr>
                            <tr>
                                <th>Cargo:</th>
                                <td>{emp.cargo}</td>
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

i_nomina = nomina()
while True:
    print("Menú")
    print("1- Agregar Empleados\n2- Mostrar Empleados\n3- Exportar un empleado\n4- Exportar todos los empleados\n5- Salir")
    opc = input("\n\nDigite una opcion: ")
    if opc == "1":
        while True:
            ced = input("\nInserte su cedula sin guiones: ")
            sal = input("\nInserte su salario: ")
            cargo = input("\nInserte su cargo: ")
            if(len(ced) >= 1):
                Empleado = empleado(ced,sal,cargo)
                i_nomina.Agregar(Empleado)
            else:
                break
    elif opc == "2":
        i_nomina.Mostrar()
    elif opc == "3":
        i_nomina.Mostrar()
        ele = input("Que empleado desea exportar: ")
        i_nomina.Exportar(ele)
    elif opc == "4":
        i_nomina.Exportar_Todos()
    elif opc == "5":
        break
    else:
        print("Debe digitar una opcion valida") 

