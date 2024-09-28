from flask import Flask, Response, jsonify
import cv2
import time
import busio
from board import SCL, SDA
from adafruit_sht31d import SHT31D
from bmp280 import BMP280

# Inicializa Flask
app = Flask(__name__)

# Inicializa I2C y sensores
i2c = busio.I2C(SCL, SDA)
sht30 = SHT31D(i2c)
bmp280 = BMP280()

# Inicializa la webcam en el andice 0
webcam = cv2.VideoCapture(2)

def get_sensor_data():
    temperature = sht30.temperature
    humidity = sht30.relative_humidity
    pressure = bmp280.get_pressure()
    return temperature, humidity, pressure

def get_frame():
    ret, frame = webcam.read()
    if not ret:
        return None
    # Codifica la imagen en formato JPEG
    return cv2.imencode('.jpg', frame)[1].tobytes()

@app.route('/video_feed')
def video_feed():
    def generate():
        while True:
            frame = get_frame()
            if frame is None:
                break
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.2)  # Aumenta el tiempo entre frames para aliviar la carga

    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/sensor_data')
def sensor_data():
    temperature, humidity, pressure = get_sensor_data()
    return jsonify(temperature=temperature, humidity=humidity, pressure=pressure)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
