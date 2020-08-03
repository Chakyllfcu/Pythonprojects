from statistics import mean 
def input_int(msg):
    tmp = 0
    try:
        tmp = int(input(msg))
    except:
        print("Solo se permite notas")
        tmp = input_int(msg)
    return tmp


print("Programa que acepte 4 notas, determinar el promedio")
#Lista donde se guardaran los valores
lst = [] 
for i in range(1, 5): 
	n = input_int(f"Inserte la nota {i} : ")
	lst.append(n)
print("El promedio es",mean(lst)) 