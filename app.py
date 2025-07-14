from flask import Flask, request, jsonify, send_from_directory
import csv
from datetime import datetime
import os

app = Flask(__name__, static_folder='frontend')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    machine = data.get('machine')
    barcode = data.get('barcode')
    timestamp = datetime.now().isoformat()

    row = [machine, barcode, timestamp]

    with open('scans.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

    return jsonify({"message": "Data saved successfully."})
