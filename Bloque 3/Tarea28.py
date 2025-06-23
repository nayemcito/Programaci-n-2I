man_a = open("mbox.txt")
contador = 0
for linea in man_a:
    if linea.startswith("From:"):
        contador += 1
print("Cantidad de líneas que empiezan con 'From:':", contador)