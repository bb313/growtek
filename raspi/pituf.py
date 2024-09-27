import time
from flask import Flask, jsonify
from smbus2 import SMBus

# Dirección I2C de los sensores
SENSOR_ENV_ADDRESS = 0x76
SENSOR_TVOC_ADDRESS = 0x5A
SENSOR_EARTH_ADDRESS = 0x77

app = Flask(__name__)

# Iniciar el bus I2C
bus = SMBus(1)

def read_temperature_humidity():
    # Aquí iría la lógica para leer los valores desde el sensor específico
    # Puedes usar una librería dedicada al sensor si la tienes, o seguir las especificaciones del datasheet
    temperature = 25.0  # Valor ficticio
    humidity = 50.0  # Valor ficticio
    return temperature, humidity

def read_tvoc_co2():
    # Leer el valor de CO2/TVOC
    tvoc = 120  # Valor ficticio
    co2 = 400  # Valor ficticio
    return tvoc, co2

@app.route('/data')
def send_sensor_data():
    temp, hum = read_temperature_humidity()
    tvoc, co2 = read_tvoc_co2()

    data = {
        'temperature': temp,
        'humidity': hum,
        'tvoc': tvoc,
        'co2': co2,
        'timestamp': time.time()
    }
    return jsonify(data)

if __name__ == "__main__":
    # Inicia el servidor Flask
    app.run(host='0.0.0.0', port=5000)
