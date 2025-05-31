#mini proyecto
def adivina_elnumero():
    print("Bienvenido al juego Descifra el Misterio Numérico para continuar con el juego")
Nombre_del_participante=input("Ingresa su nombre : ")
print(f"Hola {Nombre_del_participante} listo para jugar ")
print("¿Quieres ver las reglas del juego?")
ver_reglas = input("Escribe 'si' para verlas o cualquier otra cosa para continuar: ").lower()
if ver_reglas == "si":
    print("\n REGLAS DEL JUEGO:")
    print("- Adivina el número secreto entre 1 y 100.")
    print("- El sistema te dirá si el número es mayor o menor.")
    print("- Ganas cuando aciertas el número exacto.")
    print("- ¡Suerte!\n")
print("LISTO AHORA QUE SABES LAS REGLAS DE JUEGO EMPREZEMOS")
print("\n")
def juego_numero_secreto():
    numero_secreto = 56
    num = int(input("Adivina el número secreto (entre 1 y 100): "))
    while num != numero_secreto:
        if num < numero_secreto:
            print("El número es mayor")
        else:
            print("El número es menor")
        num = int(input("Dame un número: "))
    print("¡Felicidades! ¡Ganaste!")
juego_numero_secreto()


def calcular_promedio():
    nota1 = float(input("Ingrese la Nota 1 de 0 a 10: "))
    nota2 = float(input("Ingrese la Nota 2 de 0 a 10: "))
    nota3 = float(input("Ingrese la Nota 3 de 0 a 10: "))

    promedio = (nota1 + nota2 + nota3) / 3
  

    if promedio < 5:
        estado = "Reprobado"
    elif promedio >= 5.1  and  promedio < 6.99:
        estado = "Regular"
    elif promedio >=7 and promedio < 8.99:
        estado = "Buena"
    else:
        estado = "Excelente"

    print(f"\n El Promedio del estudiante es:  {promedio}")
    print(f"\n El estudiante se encuentra en un estado: {estado}")
calcular_promedio()

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Adivina el número")
        print("2. Calcular promedio")
        print("3. Multiplicar dos números")
        print("4. Salir")
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            adivina_elnumero()
        elif opcion == "2":
            calcular_promedio()
        elif opcion == "3":
            multiplicar()
        elif opcion == "4":
            print("¡Adiós!")
            break
        else:
            print("Opción inválida. Intenta otra vez.")

menu()