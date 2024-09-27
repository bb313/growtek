import bme680
import time

# Iniciar el sensor BME680 en la dirección I2C primaria
sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)

# Configuración del sensor
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

print("Calibrating sensor, please wait...")

# Realiza una lectura inicial para calibrar el sensor (puede tardar unos segundos)
while not sensor.get_sensor_data() or not sensor.data.heat_stable:
    time.sleep(1)

# Función para mostrar los datos en consola
def display_data():
    if sensor.get_sensor_data():
        temperature = sensor.data.temperature
        humidity = sensor.data.humidity
        pressure = sensor.data.pressure

        # Si el sensor está calibrado para medir gas, mostrar esos datos también
        if sensor.data.heat_stable:
            gas_resistance = sensor.data.gas_resistance
            print(f"Temperature: {temperature:.2f} °C, Humidity: {humidity:.2f} %, Pressure: {pressure:.2f} hPa, Gas Resistance: {gas_resistance:.2f} ohms")
        else:
            print(f"Temperature: {temperature:.2f} °C, Humidity: {humidity:.2f} %, Pressure: {pressure:.2f} hPa")

# Bucle para actualizar los datos continuamente cada 5 segundos
try:
    while True:
        display_data()
        time.sleep(5)  # Actualización cada 5 segundos
except KeyboardInterrupt:
    print("Terminado.")

