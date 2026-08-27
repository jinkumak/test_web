from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__)

DATA_FILE = "data/location.json"


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/location", methods=["POST"])
def save_location():

    data = request.get_json()

    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("Location saved:")
    print(data)

    return jsonify({
        "status": "success",
        "message": "Location saved"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
