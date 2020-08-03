
print("Programa que acepte una frase, determinar la cantidad de vocales que contiene la misma.\n")

n = input("Inserte una frase:\n\n")

minuscula = n.lower()
cuenta_vocales = {}

for vocal in "aeiou":
    contador = minuscula.count(vocal)
    cuenta_vocales[vocal] = contador

c = cuenta_vocales.values()
tmp = sum(c)

print(f"La frase tiene {tmp} vocales.")