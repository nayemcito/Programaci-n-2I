import math

# Parámetros
N = int(input("Ingrese el tamaño de la población: "))  # Tamaño de la población
Z = 1.96  # Valor Z para un nivel de confianza del 95%
p = 0.5   # Proporción esperada
q = 1 - p
e = 0.04  # Margen de error (4%)

# Cálculo del tamaño de la muestra
n = (N * Z**2 * p * q) / ((N - 1) * e**2 + Z**2 * p * q)

print(f"Tamaño de la muestra recomendado: {math.ceil(n)}")