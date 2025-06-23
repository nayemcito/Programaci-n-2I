# Diccionario con productos y precios
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





