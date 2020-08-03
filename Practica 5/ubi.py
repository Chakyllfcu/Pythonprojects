def exportartodos():
	print("Aquí puedes expotar a todos")
    #Abro el archivo en Escritura
	archivo = open('estudiantes.html', 'w', encoding="utf-8")
	html = f"""
	<html>
		<head>
		<body>
			<center>
				<h3>Datos Estudiantes</h3>
            """
    archivo.write(html)
	archivo.close()
    #Lo cierro para que ya este guardado en la ubicacion

	for personas in datos:
        #Abro el archivo en concatenacion
        archivo = open('estudiantes.html', 'a', encoding="utf-8")
		html = f"""
		<h4>Cédula: {personas['cedula']}</h4>
		<h4>Nombre: {personas['nombre']}</h4>
		<h4>Apellido: {personas['apellido']}</h4>
		<h4>Nota 1: {personas['nota_1']}</h4>
		<h4>Nota 2: {personas['nota_2']}</h4>
		<h4>Promedio: {personas['promedio']}</h4>
        """
        archivo.write(html)
        #Lo cierro cada vez que termine para que cada vez que el for de la vuelta coloque la informacion de la siguiente persona debajo de la otra
	    archivo.close()


    #finalmente lo abres una vez mas en concatenacion para que el cierre del html se ponga debajo de todas las personas que el for inserto.
    archivo = open('estudiantes.html', 'a', encoding="utf-8")
    html = f"""
    			</center> 
		</body>
		</head>	
	</html>
	"""
	nombre_archivo = 'file:///Users/Ubi/Desktop/Practica 5/' + 'estudiantes.html'
	archivo.write(html)
	archivo.close()
	webbrowser.open_new_tab(nombre_archivo)