man_a = open("mbox.txt")
contador = 0
for linea in man_a:
    palabras = linea.split()
    contador += len(palabras)
print("Cantidad total de palabras en el archivo:", contador)