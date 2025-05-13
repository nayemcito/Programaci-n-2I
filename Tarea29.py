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

#4Simular un cajero automático (menú: retirar, depositar, salir).

#5Calcular la raíz cuadrada por aproximación (método babilónico).

#6Contar dígitos de un número entero (ej: 456 → 3).

#7Generar la secuencia de Fibonacci hasta un límite.

#8Encontrar números primos en un rango dado.

#9Simular un temporizador (contar regresivamente desde N).

#10Leer archivos línea por línea hasta fin de archivo.

#MIENTRAS - WHILE
# Visualizar los primeros números con mientras - while

contador = 0
while contador <=5:
    print("Numero:",contador )
    contador +=1
