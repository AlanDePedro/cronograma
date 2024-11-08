import pandas as pd
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Tu SID de cuenta y Auth Token de Twilio (coloca tu propio token y SID)
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Leer el archivo Excel
cronograma_df = pd.read_excel('cronograma_empleados.xlsx')

# Verificar si hay valores nulos en la columna 'Fecha' y reemplazarlos con la fecha anterior
for i in range(1, len(cronograma_df)):
    if pd.isna(cronograma_df.loc[i, 'Fecha']):
        cronograma_df.loc[i, 'Fecha'] = cronograma_df.loc[i - 1, 'Fecha']

# Convertir las filas a un formato de mensaje
mensaje_final = ""
for index, row in cronograma_df.iterrows():
    mensaje = f"📅 Fecha: {row['Fecha']}\nHora: {row['Hora']}\nEmpleado: {row['Empleado/s']}\nMercado: {row['Mercado/s']}\nCamión: {row['Camión']}\n\n"
    mensaje_final += mensaje  # Añadir mensaje al mensaje final

# Comprobar el tamaño del mensaje antes de enviarlo
max_length = 1500  # Límite de caracteres para Twilio

# Dividir el mensaje en fragmentos de 1500 caracteres si es necesario
def dividir_mensaje(mensaje, limite=1500):
    return [mensaje[i:i+limite] for i in range(0, len(mensaje), limite)]

# Dividir el mensaje en fragmentos si es necesario
mensajes = dividir_mensaje(mensaje_final, max_length)

# Enviar cada fragmento
for i, fragmento in enumerate(mensajes):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=fragmento,
            to='whatsapp:+5491165189669'
        )
        print(f"Mensaje {i+1} enviado: {message.sid}")
    except Exception as e:
        print(f"Error al enviar el mensaje parcial {i+1}: {e}")