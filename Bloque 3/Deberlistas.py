#1 Creamos una lista con al menos 5 elementos
frutas = ["Manzana", "Banana", "Cereza", "Durazno", "Uva"]

# Recorremos la lista usando un bucle for con enumerate para obtener el índice y el elemento
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

#2 Bucle para asegurarse de que el usuario ingrese al menos 3 palabras
while True:
    entrada = input("Ingresa al menos 3 palabras separadas por espacios: ")
    palabras = entrada.split()

    if len(palabras) >= 3:
        break
    else:
        print("⚠️ Debes ingresar al menos 3 palabras. Intenta de nuevo.\n")

# Encontrar la palabra más larga
palabra_mas_larga = max(palabras, key=len)

# Mostrar el resultado
print(f"La palabra más larga es: {palabra_mas_larga}")


#3 Pedir al usuario una línea de texto
linea = input("Escribe una línea de texto: ")

# Separar las palabras por espacios
palabras = linea.lower().split()

# Crear el diccionario para contar las frecuencias
frecuencia = {}

# Contar cada palabra
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

# Mostrar los resultados
print("\nFrecuencia de palabras:")
for palabra, conteo in frecuencia.items():
    print(f"{palabra}: {conteo}")

#4 Lee un archivo de texto `datos.txt` y muestra las 3 palabras más repetidas utilizando un diccionario.

frecuencias = {}
with open("mbox.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        for palabra in linea.lower().split():
            p = palabra.strip(".,;:¿?¡!()[]{}\"'")
            if p:
                frecuencias[p] = frecuencias.get(p, 0) + 1

# Imprimir en el mismo formato que tu ejemplo
print("Top 3 palabras más frecuentes:")
for palabra, cantidad in sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(f"{palabra}: {cantidad} veces")


#5 Diccionario con productos y precios
tienda = {
    "laptop": 899.99,
    "teclado": 49.50,
    "ratón": 25.00,
    "monitor": 179.99,
    "auriculares": 89.90
}

# Convertimos a lista para numerar fácilmente
productos = list(tienda.items())

# Mostrar lista numerada de productos
print(" Bienvenido a la tienda virtual")
print("Productos disponibles:")
for i, (nombre, precio) in enumerate(productos, 1):
    print(f"{i}. {nombre.title()} — ${precio:.2f}")

# Solicitar opción al usuario
while True:
    seleccion = input("\nElige un producto por su número (o escribe '0' para salir): ")
    
    if seleccion == "0":
        print("¡Gracias por visitar la tienda!")
        break
    elif seleccion.isdigit() and 1 <= int(seleccion) <= len(productos):
        nombre, precio = productos[int(seleccion) - 1]
        print(f" Elegiste {nombre.title()}, su precio es: ${precio:.2f}")
    else:
        print(" Opción inválida. Ingresa un número válido.")