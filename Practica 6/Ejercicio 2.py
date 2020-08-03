from requests import get

class persona:
    cedula = '-'
    salario = 0.0
    nombre = 'n/a'
    apellido = 'n/a'

    def __init__(self,cedula, salario, nombre = "",apellido = ""):
        self.cedula = cedula
        self.salario = salario
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

lpersona = []

while True:
    ced = input("Inserte su cedula sin guiones: ")
    sal = input("Inserte su salario: ")
    if(len(ced)>10):
        Persona = persona(ced,sal)
        lpersona.append(Persona)
    else:
        print("Debe insertar datos validos")
        break

for i in lpersona:
    print(f"{i.nombre} {i.apellido} Salario : RD${i.salario}")
