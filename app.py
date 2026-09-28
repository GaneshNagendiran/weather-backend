from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Weather API Server is running"


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "weather-backend"
    })


@app.route("/weather")
def weather():
    return jsonify({
        "city": "Bengaluru",
        "temperature": "28°C",
        "condition": "Partly Cloudy",
        "humidity": "65%",
        "wind_speed": "12 km/h"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
