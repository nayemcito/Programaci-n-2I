# Crea un mini programa que use al menos 3 funciones. Algunas ideas:
def menu():
    print("1. Calculadora básica")
    print("2. Convertir temperatura")
    print("3. calcular promedio")
    print("4. Salir")
    
def calculadora_basica():
    print("Bienvenido a la calculadora básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
def canvertir(valor, temp):
    if temp == 'C':
        return str((valor * 9/5) + 32) + " Fahrenheit"
    elif temp == 'F':
        return str((valor - 32) * 5/9) + " Celsius"
def calcular_promedio():
    nota1 = float(input("Ingrese la Nota 1 de 0 a 10: "))
    nota2 = float(input("Ingrese la Nota 2 de 0 a 10: "))
    nota3 = float(input("Ingrese la Nota 3 de 0 a 10: "))
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

while True:
    menu()
    opcion=input("Ingrese la opcion (1-4): ")

    if opcion == "1":
        calculadora_basica()
        while True:
            opcion = input("Elige una opción (1-5): ")
            if opcion == "5":
                print("Gracias por utilizar esta calculadora.")
                break
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            if opcion not in ["1", "2", "3", "4", "5"]:
                print("Opción no válida, intenta de nuevo.")
                continue
            elif opcion in ["1", "2", "3", "4"]:
                if opcion == "1":
                    resultado = num1 + num2
                    print(f"Resultado: {resultado}")
                elif opcion == "2":
                    resultado = num1 - num2
                    print(f"Resultado: {resultado}")
                elif opcion == "3":
                    resultado = num1 * num2
                    print(f"Resultado: {resultado}")
                elif opcion == "4":
                    if num2 != 0:
                        resultado = num1 / num2
                        print(f"Resultado: {resultado}")
                    else:
                        print("Error: División por cero.")
    elif opcion == "2":
        valor = float(input("Ingrese el valor de la temperatura: "))
        temp = input("Ingrese: C para cambiar de C a F, F para cambiar de F a C: ").upper()
        print("El valor convertido es: ", canvertir(valor, temp))
    elif opcion == "3":
        promedio = calcular_promedio()
        if promedio < 5:
            estado = "Reprobado"
        elif promedio >= 5.1 and promedio < 6.99:
            estado = "Regular"
        elif promedio >= 7 and promedio < 8.99:
            estado = "Buena"
        else:
            estado = "Excelente"

        print(f"\n El Promedio del estudiante es:  {promedio}")
        print(f" El estudiante se encuentra en un estado: {estado}")
    elif opcion == "4":
        print ("GRACIAS POR INGRESAR AL MINI PROYECTO")
        break
