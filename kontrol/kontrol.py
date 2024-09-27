from flask import Flask, render_template, jsonify
import requests
import threading
import time

app = Flask(__name__)

sensor_data = []

def fetch_sensor_data():
    global sensor_data
    while True:
        try:
            # Reemplaza con la IP de tu Raspberry Pi
            response = requests.get('http://<Raspberry_Pi_IP>:5000/data')
            if response.status_code == 200:
                sensor_data.append(response.json())
        except Exception as e:
            print(f"Error fetching data: {e}")
        time.sleep(10)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensor_data')
def get_sensor_data():
    return jsonify(sensor_data)

if __name__ == "__main__":
    threading.Thread(target=fetch_sensor_data, daemon=True).start()
    app.run(host='0.0.0.0', port=8080)
