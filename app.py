from flask import Flask, jsonify
import json
import numpy as np

app = Flask(__name__)

@app.route('/metrics')
def get_metrics():
    with open('metrics.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/predict')
def predict_load():
    with open('metrics.json', 'r') as f:
        data = json.load(f)

    # Extract CPU values
    cpu_values = [dp["Average"] for dp in data.get("Datapoints", []) if "Average" in dp]

    if not cpu_values:
        return jsonify({"error": "No CPU data found"})

    # Simple predictive logic (moving average)
    avg_load = np.mean(cpu_values)
    predicted_load = avg_load * 1.15  # assume 15% growth

    return jsonify({
        "current_avg": avg_load,
        "predicted_next": predicted_load,
        "recommendation": "Scale Up" if predicted_load > 60 else "Scale Down" if predicted_load < 20 else "Maintain"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


