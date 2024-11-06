import pandas as pd

# Leer el archivo Excel y eliminar la columna 'Día' si existe
df = pd.read_excel("cronograma_empleados.xlsx")

if "Día" in df.columns:
    df = df.drop(columns=["Día"])

def agregar_mercado():
    global df  # Declarar df como global antes de usarla
    
    # Recorremos las filas y agregamos solo las que están completas
    for index, row in df.iterrows():
        if pd.notna(row["Fecha"]) and pd.notna(row["Mercado/s"]):
            # Si hay fecha y mercado (es decir, la fila está completa), agregamos el mercado
            fecha = row["Fecha"]
            mercado = row["Mercado/s"]
            hora = row["Hora"] if pd.notna(row["Hora"]) else ""  # Si no hay hora, dejamos vacío
            camion = row["Camión"] if pd.notna(row["Camión"]) else ""  # Si no hay camión, dejamos vacío
            empleado = row["Empleado/s"] if pd.notna(row["Empleado/s"]) else ""  # Lo mismo para el empleado

            # Verificamos si la fecha ya existe
            if not (df["Fecha"] == fecha).any():
                # Si la fecha no existe, agregar una nueva fila con la fecha
                nuevo_mercado = {
                    "Fecha": fecha,
                    "Mercado/s": mercado,
                    "Hora": hora,
                    "Camión": camion,
                    "Empleado/s": empleado
                }
                nuevo_df = pd.DataFrame([nuevo_mercado])
                df = pd.concat([df, nuevo_df], ignore_index=True)
            else:
                # Si la fecha ya existe, se agregan los datos
                for idx, r in df.iterrows():
                    if r["Fecha"] == fecha:
                        if pd.isna(df.at[idx, "Mercado/s"]):  # Si el campo Mercado está vacío, se agrega
                            df.at[idx, "Mercado/s"] = mercado
                            df.at[idx, "Hora"] = hora
                            df.at[idx, "Camión"] = camion
                            df.at[idx, "Empleado/s"] = empleado
                            break
                        else:
                            # Si ya existe mercado en esa fila, agregarlo en la siguiente fila
                            nuevo_mercado = {
                                "Fecha": "",  # No se repite la fecha
                                "Mercado/s": mercado,
                                "Hora": hora,
                                "Camión": camion,
                                "Empleado/s": empleado
                            }
                            nuevo_df = pd.DataFrame([nuevo_mercado])
                            df = pd.concat([df, nuevo_df], ignore_index=True)
                            break

    # Guardar el DataFrame actualizado en el archivo Excel
    df.to_excel("cronograma_empleados.xlsx", index=False)

def eliminar_mercado(fecha, *mercados):
    global df  # Declarar df como global antes de usarla
    for mercado in mercados:
        df = df[~((df["Fecha"] == fecha) & (df["Mercado/s"] == mercado))]
    df.to_excel("cronograma_empleados.xlsx", index=False)

def actualizar_mercado(fecha, mercado, nueva_hora, nuevo_camion, nuevo_empleado):
    global df  # Declarar df como global antes de usarla
    for index, row in df.iterrows():
        if row["Fecha"] == fecha and str(row["Mercado/s"]).strip() == str(mercado).strip():
            # Actualizar la hora, camión y empleado de ese mercado
            df.at[index, "Hora"] = nueva_hora
            df.at[index, "Camión"] = nuevo_camion
            df.at[index, "Empleado/s"] = nuevo_empleado
            # Guardar el DataFrame en el archivo Excel
            df.to_excel("cronograma_empleados.xlsx", index=False)
            print(f"Mercado '{mercado}' actualizado.")
            break
    else:
        print(f"No se encontró el mercado '{mercado}' en la fecha {fecha} para actualizar.")

# Ejemplo de agregar mercados con los datos vacíos en el archivo Excel
agregar_mercado()

# Ejemplo de eliminar mercados en una fecha
# eliminar_mercado("2024-11-17", "Mercado 43", "Mercado 50")

print("Operaciones de ejemplo completadas.")