import tkinter as tk
from PIL import Image, ImageTk
import requests
import time
import threading
from io import BytesIO

# URL de la Raspberry Pi
RPI_URL = 'http://10.23.0.103:5000'  # Asegúrate de incluir 'http://'

def update_image():
    while True:
        try:
            # Obtén el flujo de video
            video_url = f"{RPI_URL}/video_feed"
            response = requests.get(video_url, stream=True, timeout=5)

            if response.status_code == 200:
                # Lee los datos del stream y crea una imagen
                img_data = BytesIO(response.raw.read(1024*1024))  # Ajusta el tamaño si es necesario
                img = Image.open(img_data).convert("RGB")  # Asegúrate de que la imagen esté en RGB
                imgtk = ImageTk.PhotoImage(image=img)
                
                # Actualiza la imagen en el label
                image_label.imgtk = imgtk
                image_label.configure(image=imgtk)
            else:
                print("Error en el stream de video:", response.status_code)
        except Exception as e:
            print("Error al obtener video:", e)

        time.sleep(0.1)  # Controla la tasa de actualización

def update_sensor_data():
    while True:
        try:
            # Obtiene los datos del sensor
            response = requests.get(f"{RPI_URL}/sensor_data", timeout=5)
            if response.status_code == 200:
                sensor_data = response.json()
                
                # Actualiza los datos del sensor
                temp_label.config(text=f'Temperature: {sensor_data["temperature"]:.2f} °C')
                humidity_label.config(text=f'Humidity: {sensor_data["humidity"]:.2f} %')
                pressure_label.config(text=f'Pressure: {sensor_data["pressure"]:.2f} hPa')
            else:
                print("Error en los datos del sensor:", response.status_code)
        except Exception as e:
            print("Error al obtener datos del sensor:", e)

        time.sleep(3)  # Actualiza los datos cada 3 segundos

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Webcam and Sensor Data")

# Label para la imagen de la webcam
image_label = tk.Label(root)
image_label.pack()

# Labels para los datos de los sensores
temp_label = tk.Label(root)
temp_label.pack()

humidity_label = tk.Label(root)
humidity_label.pack()

pressure_label = tk.Label(root)
pressure_label.pack()

# Inicia hilos para actualizar imágenes y datos del sensor
threading.Thread(target=update_image, daemon=True).start()
threading.Thread(target=update_sensor_data, daemon=True).start()

# Ejecuta la interfaz gráfica
root.mainloop()
