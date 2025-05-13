#Sumar números ingresados por el usuario hasta que ingrese 0.
#Adivinar un número aleatorio entre 1 y 100 (pistas: "mayor" o "menor").
#Validar contraseña (repetir hasta que coincida con una guardada).
#Simular un cajero automático (menú: retirar, depositar, salir).
#Calcular la raíz cuadrada por aproximación (método babilónico).
#Contar dígitos de un número entero (ej: 456 → 3).
#Generar la secuencia de Fibonacci hasta un límite.
#Encontrar números primos en un rango dado.
#Simular un temporizador (contar regresivamente desde N).
#Leer archivos línea por línea hasta fin de archivo.
print("\n4. Bienvenido:")
dinerodisponible = 1000
opcion = ""
while opcion != "3":
    print("1. Retirar")
    print("2. Depositar")
    print("3. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        monto = float(input("Monto a retirar: "))
        if monto <= dinerodisponible:
            dinerodisponible -= monto
            print(f"Nuevo saldo: {dinerodisponible}")
        else:
            print("Fondos insuficientes.")
    elif opcion == "2":
        monto = float(input("Monto a depositar: "))
        dinerodisponible += monto
        print(f"Nuevo saldo: {dinerodisponible}")
print("Sesión finalizada.")
