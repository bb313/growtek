import tkinter as tk
from smbus2 import SMBus
import time

# Crear la ventana principal
root = tk.Tk()
root.title("Sensor Dashboard")

# Definir etiquetas para mostrar los datos de los sensores
temp_label = tk.Label(root, text="Temperature: --", font=("Helvetica", 16))
hum_label = tk.Label(root, text="Humidity: --", font=("Helvetica", 16))
tvoc_label = tk.Label(root, text="TVOC: --", font=("Helvetica", 16))
co2_label = tk.Label(root, text="CO2: --", font=("Helvetica", 16))

# Colocar las etiquetas en la ventana
temp_label.pack(pady=10)
hum_label.pack(pady=10)
tvoc_label.pack(pady=10)
co2_label.pack(pady=10)

# Dirección I2C de los sensores
SENSOR_ENV_ADDRESS = 0x76  # M5Stack Environment Sensor II (ejemplo)
SENSOR_TVOC_ADDRESS = 0x5A  # TVOC/eCO2 Sensor
SENSOR_EARTH_ADDRESS = 0x77  # Earth Sensor (ejemplo)

# Iniciar el bus I2C
bus = SMBus(1)

# Funciones para leer los datos de los sensores
def read_temperature_humidity():
    # Aquí iría la lógica para leer los valores de temperatura y humedad desde el sensor
    temperature = 25.0  # Valor ficticio
    humidity = 50.0  # Valor ficticio
    return temperature, humidity

def read_tvoc_co2():
    # Leer el valor de CO2/TVOC
    tvoc = 120  # Valor ficticio
    co2 = 400  # Valor ficticio
    return tvoc, co2

def update_data():
    # Leer los datos de los sensores
    temp, hum = read_temperature_humidity()
    tvoc, co2 = read_tvoc_co2()

    # Actualizar las etiquetas con los nuevos valores
    temp_label.config(text=f"Temperature: {temp:.2f} °C")
    hum_label.config(text=f"Humidity: {hum:.2f} %")
    tvoc_label.config(text=f"TVOC: {tvoc} ppb")
    co2_label.config(text=f"CO2: {co2} ppm")

    # Actualizar los datos cada 5 segundos
    root.after(5000, update_data)

# Iniciar la actualización de datos
update_data()

# Ejecutar el loop principal de la interfaz gráfica
root.mainloop()
