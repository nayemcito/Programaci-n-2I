#EJERCICIO 1: Analisis de la temperatura a lo largo de una semana 
import plotly.express as px

# Datos de ejemplo
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = [22, 24, 19, 23, 26, 27, 25]  # Temperaturas en grados Celsius

# Crear el gráfico de líneas
fig = px.line(x=dias, y=temperaturas, markers=True,
              labels={"x": "Día", "y": "Temperatura (°C)"},
              title="Variación de Temperatura a lo Largo de la Semana")

# Mostrar el gráfico
fig.show()


#EJERCICIO 2: Resistencia de materiales
import plotly.express as px

tipos = ["H10", "H20", "H30", "H40"]
resistencia = [150, 220, 280, 340]

fig = px.bar(x=tipos, y=resistencia, labels={"x":"Tipo de Hormigón", "y":"Resistencia (kg/cm²)"},
             title="Resistencia de Diferentes Tipos de Hormigón")
fig.show()


#EJERCICIO 3: Evolvución de carga en obra
import plotly.express as px

etapas = ["Cimentación", "Estructura", "Acabados", "Techo"]
carga = [500, 1200, 800, 1400]

fig = px.line(x=etapas, y=carga, markers=True,
              labels={"x":"Etapa", "y":"Carga (kg)"},
              title="Evolución de Carga en el Proceso Constructivo")
fig.show()

#EJERCICIO 4: distribucio de uso de espacios
import plotly.express as px

etiquetas = ["Oficinas", "Pasillos", "Salas técnicas", "Baños"]
porcentajes = [45, 25, 20, 10]

fig = px.pie(names=etiquetas, values=porcentajes,
             title="Distribución de Espacios en Proyecto Edificatorio")
fig.show()


#EJERCICIO 5: 2D: ubicacion de sensores estructurales
import plotly.express as px

x = [2, 4, 6, 8]
y = [1, 3, 5, 2]
nombres = ["Sensor A", "Sensor B", "Sensor C", "Sensor D"]

fig = px.scatter(x=x, y=y, text=nombres, labels={"x":"Eje X (m)", "y":"Eje Y (m)"},
                 title="Ubicación de Sensores en Losa")
fig.update_traces(textposition='top center', marker_size=12)
fig.show()
