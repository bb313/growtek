import time
import board
import busio
import adafruit_bme680

# Inicializar I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Inicializar el sensor BME680
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)

# Opcional: Configurar la temperatura en grados Celsius (por defecto)
sensor.sea_level_pressure = 1013.25  # Ajusta según sea necesario

# Función para mostrar los datos del sensor
def display_data():
    temperature = sensor.temperature
    gas = sensor.gas
    humidity = sensor.humidity
    pressure = sensor.pressure

    print(f"Temperature: {temperature:.2f} °C, Humidity: {humidity:.2f} %, Pressure: {pressure:.2f} hPa, Gas: {gas:.2f} ohms")

# Bucle para actualizar los datos continuamente
try:
    while True:
        display_data()
        time.sleep(5)  # Actualiza cada 5 segundos
except KeyboardInterrupt:
    print("Terminado.")
