import os

def crear_archivo_automatico():
    nombre = "archivo1.txt"
    with open(nombre, "w", encoding="utf-8") as archivo:
        print(f"Archivo '{nombre}' creado automáticamente.")

def crear_archivo():
    nombre = input("Nombre del archivo a crear (ejemplo.txt): ")
    with open(nombre, "w", encoding="utf-8") as archivo:
        print(f"Archivo '{nombre}' creado correctamente.")

def escribir_archivo():
    nombre = input("Nombre del archivo para escribir: ")
    if os.path.exists(nombre):
        texto = input("Escribe el texto que deseas agregar:\n")
        with open(nombre, "a", encoding="utf-8") as archivo:
            archivo.write(texto + "\n")
        print("Texto agregado correctamente.")
    else:
        print("El archivo no existe.")

def eliminar_archivo():
    nombre = input("Nombre del archivo a eliminar: ")
    if os.path.exists(nombre):
        os.remove(nombre)
        print(f"Archivo '{nombre}' eliminado correctamente.")
    else:
        print("El archivo no existe.")

def menu():
    while True:
        print("\n--- MENÚ DE ARCHIVOS ---")
        print("1. Crear archivo 'archivo1.txt'")
        print("2. Crear archivo nuevo")
        print("3. Escribir en archivo")
        print("4. Eliminar archivo")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            crear_archivo_automatico()
        elif opcion == "2":
            crear_archivo()
        elif opcion == "3":
            escribir_archivo()
        elif opcion == "4":
            eliminar_archivo()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()