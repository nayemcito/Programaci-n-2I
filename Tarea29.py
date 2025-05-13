#1Sumar números ingresados por el usuario hasta que ingrese 0.
suma = 0
numero = int(input("Ingresa un número (0 para terminar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingresa otro número (0 para terminar): "))

print("La suma total es:", suma)

#2Adivinar un número aleatorio entre 1 y 100 (pistas: "mayor" o "menor").

n = 30
print("Adivina el número (1-100)")
i = 0

while i != n:
    i = int(input("Tu intento: "))
    if i < n:
        print("Mayor")
    elif i > n:
        print("Menor")

print("¡Correcto!")
#3Validar contraseña (repetir hasta que coincida con una guardada).

print("\n3. Validar contraseña:")
contraseña_correcta = "2222"
entrada = ""

while entrada != contraseña_correcta:
    entrada = input("Ingresa la contraseña: ")
    if entrada != contraseña_correcta:
        print("Contraseña incorrecta. Intenta de nuevo.")

print("Contraseña válida... ingresando a su cuenta")



#4Simular un cajero automático (menú: retirar, depositar, salir).

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


#5Calcular la raíz cuadrada por aproximación (método babilónico).
valor = 20
epsilon = 0.0001
epsilon_elevadoalcuadrado= epsilon ** 2
aprox = valor / 2
nuevo_aprox = 0.5 * (aprox + valor / aprox)

while (nuevo_aprox - aprox) ** 2 >= epsilon_elevadoalcuadrado:
    aprox = nuevo_aprox
    nuevo_aprox = 0.5 * (aprox + valor / aprox)

print(f"La raíz cuadrada aproximada de {valor} es {nuevo_aprox}")

#6Contar dígitos de un número entero (ej: 456 → 3).
numero_entero = 456
temporal = numero_entero
digitos = 0

while temporal > 0:
    temporal //= 10
    digitos += 1

print(f"El número {numero_entero} tiene {digitos} dígitos.")

#7Generar la secuencia de Fibonacci hasta un límite.
limitemaximo = int(input("Introduce el límite: "))
x, y = 0, 1
fibonacci = [x]

while x <= limitemaximo:
    x, y = y, x + y
    if x <= limitemaximo:
        fibonacci.append(x)

print(f"Sucesión de Fibonacci hasta {limitemaximo}:")
print(fibonacci)

#8Encontrar números primos en un rango dado.
rangoinicial = 10
rangofinal = 50
actual = rangoinicial

while actual <= rangofinal:
    if actual > 1:
        divisor = 2
        primo = True
        while divisor * divisor <= actual:
            if actual % divisor == 0:
                primo = False
                break
            divisor += 1
        if primo:
            print(actual)
    actual += 1

#9Simular un temporizador (contar regresivamente desde N).
cuenta_regresiva = int(input("Introduce un número para iniciar la cuenta regresiva: "))

while cuenta_regresiva > 0:
    print(f"Tiempo restante: {cuenta_regresiva} segundos")
    cuenta_regresiva -= 1

print("¡Cuenta regresiva completada!")

#10Leer archivos línea por línea hasta fin de archivo.
f = open("Nuevo Documento de texto.txt", "r")
linea = f.readline()
while linea != "":
    print(linea, end="")
    linea = f.readline()
f.close()
print("fin del programa")
#MIENTRAS - WHILE
# Visualizar los primeros números con mientras - while

contador = 0
while contador <=5:
    print("Numero:",contador )
    contador +=1
