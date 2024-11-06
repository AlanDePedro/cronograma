import pandas as pd

# Definir la estructura del DataFrame
data = {
    "Fecha": [],          # Columna para la fecha
    "Empleado/s": [],     # Columna para los empleados
    "Mercado/s": [],      # Columna para los mercados
    "Hora": [],           # Columna para la hora de salida
    "Camión": [],         # Columna para la patente del camión
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel
df.to_excel("cronograma_empleados.xlsx", index=False)

print("Archivo 'cronograma_empleados.xlsx' creado exitosamente.")