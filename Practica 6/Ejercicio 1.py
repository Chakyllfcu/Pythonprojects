from requests import get
from datetime import date

class persona:
    cedula = '-'
    nombre = 'n/a'
    apellido = 'n/a'
    fechanacimiento = ''


    def __init__(self,cedula,nombre = "",apellido = ""):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido

    def cargar_datos(self):
        url = "https://api.adamix.net/apec/cedula/"+self.cedula
        datos = get(url).json()
        self.nombre = datos['Nombres']
        self.apellido = datos['Apellido1'] +' '+datos['Apellido2']
        self.fechanacimiento = datos['FechaNacimiento']


    def edad(self):
        y = int(self.fechanacimiento[0:4])
        m = int(self.fechanacimiento[5:7])
        d = int(self.fechanacimiento[8:10])
        fecha = date(y,m,d)
        edad = int(abs(date.today()-fecha).days/365.25)
        print(f"La edad de usted es {edad} años.")


    def zodiaco(self,mes,dia):
        if mes == 12: 
            signo = 'Sagitario' if (dia < 22) else 'Capricornio'

        elif mes == 1: 
            signo = 'Capricornio' if (dia < 20) else 'Aquario'
    
        elif mes == 2: 
            signo = 'Aquario' if (dia < 19) else 'Piscis'
            
        elif mes == 3: 
            signo = 'Piscis' if (dia < 21) else 'Aries'
            
        elif mes == 4: 
            signo = 'Aries' if (dia < 20) else 'Tauro'
            
        elif mes == 5: 
            signo = 'Tauro' if (dia < 21) else 'Geminis'
            
        elif mes == 6: 
            signo = 'Geminis' if (dia < 21) else 'Cancer'
            
        elif mes == 7: 
            signo = 'Cancer' if (dia < 23) else 'Leo'
            
        elif mes == 8: 
            signo = 'Leo' if (dia < 23) else 'Virgo'
            
        elif mes == 9: 
            signo = 'Virgo' if (dia < 23) else 'Libra'
            
        elif mes == 10: 
            signo = 'Libra' if (dia < 23) else 'Escorpio'
            
        elif mes == 11: 
            signo = 'Escorpio' if (dia < 22) else 'Sagitario'
        print(f"Su signo zodiacal es : {signo}")

lpersona = []

Persona = persona('40210326159')
Persona.cargar_datos()
lpersona.append(Persona)

for i in lpersona:
    print(f"{i.nombre} {i.apellido} {i.fechanacimiento}")

Persona.edad()
Persona.zodiaco(int(Persona.fechanacimiento[5:7]),int(Persona.fechanacimiento[8:10]))