import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Crear una matriz simulada de cargas (por ejemplo, en kg/m²)
np.random.seed(42)
carga = np.random.randint(300, 1200, size=(8, 10))

# Convertimos en DataFrame para mejor visualización
df = pd.DataFrame(carga, columns=[f'Col{i+1}' for i in range(10)], index=[f'Fila{i+1}' for i in range(8)])

# Crear el heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, fmt="d", cmap="YlOrRd")
plt.title("Distribución de Carga en Losa (kg/m²)")
plt.xlabel("Columnas")
plt.ylabel("Filas")
plt.tight_layout()
plt.show()
