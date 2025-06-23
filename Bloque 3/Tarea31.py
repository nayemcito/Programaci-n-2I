man_a = open("mbox.txt")
linea_mas_larga = ""
for linea in man_a:
    if len(linea) > len(linea_mas_larga):
        linea_mas_larga = linea
print("La línea más larga es:")
print(linea_mas_larga)