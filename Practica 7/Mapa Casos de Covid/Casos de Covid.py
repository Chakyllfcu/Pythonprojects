import os
from peewee import *
from datetime import date
import folium

def my_input(msg, valor=False):
    tmp = input(msg)
    if(len(tmp)<1):
        if  valor == False:
            print("Debe escribir un valor valido en el campo")
            tmp = my_input(msg)
        else:
            tmp = valor
    return tmp


db = SqliteDatabase('covid.db')


class Paciente(Model):
    nombre = CharField(50)
    apellido = CharField(50)
    fecha = DateField()
    activo = SmallIntegerField()
    ubicacion = CharField(100)
    lat = CharField(20)
    lng = CharField(20)
    comentario = TextField()
    class Meta:
        database = db

db.connect()

db.create_tables([Paciente])

def agregar():
    print("Vamos a agregar un caso\n")
    p = Paciente()
    p.nombre = my_input("Digite el nombre: ")
    p.apellido = my_input("Digite el apellido: ")
    p.fecha = date.today()
    p.activo = 1
    p.ubicacion = my_input("Digite la ubicacion: ")
    p.lat = my_input("Digite la latitud(Ejemplo:18.48): ")
    p.lng = my_input("Digite la longitud(Ejemplo:-69.87): ")
    p.comentario = my_input("Coloque un comentario: ")
    p.save()
    input("Caso guardado, PRESIONE ENTER PARA CONTINUAR")

def editar():
    print("Vamos a editar un caso\n")
    for pas in Paciente.select():
        print(f"{pas.id}- {pas.nombre} {pas.apellido}")
    tmp = input("Digite el numero del caso que desea editar : ")

    pas = Paciente.get_by_id(tmp)

    pas.nombre = my_input(f"{pas.nombre}=> Digite el nuevo nombre: ")
    pas.apellido = my_input(f"{pas.apellido}=> Digite el nuevo apellido: ")
    pas.ubicacion = my_input(f"{pas.ubicacion}=> Digite la nueva ubicacion: ")
    pas.lat = my_input(f"{pas.lat}=> Digite la nueva latitud: ")
    pas.lng = my_input(f"{pas.lng}=> Digite el nuevo nombre: ")
    pas.save()
    input("El Caso se edito con exito, PRESIONE ENTER PARA CONTINUAR")


def exportar():
    print("Vamos a exportar los datos\n")
    fm = folium.Map(location=[18.94,-70.28], zoom_start=13, titles="Casos de Covid en Republica Dominicana")
    for pas in Paciente.select():
        folium.Marker(location=[pas.lat,pas.lng], tooltip='Click para ver el paciente', popup=pas.nombre+' '+pas.apellido, icon=folium.Icon(color='red', icon='info-sign')).add_to(fm)
    fm.save("Mapa_Casos_Covid.html")
    os.system("Mapa_Casos_Covid.html")


while True: #Menu
    os.system('cls')
    print("Bienvenido al programa de registro de COVID en RD")
    print("1-Agregar casos\n2-Editar casos\n3-Ver casos en el mapa\n4-Salir")
    tmp = input("Digite la opcion que desea: ")

    if tmp == '1':
        agregar()
    elif tmp == '2':
        editar()
    elif tmp == '3':
        exportar()
    elif tmp == '4':
        print("Hasta pronto :)")
        db.close()
        break
    else:
        input("Debe digitar una opcion valida, PRESIONE ENTER PARA CONTINUAR")