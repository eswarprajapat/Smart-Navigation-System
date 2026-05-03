from flask import Flask, render_template, jsonify
import random # Simulating data for the prototype

app = Flask(__name__)

# Simulated Pothole Database (Latitude, Longitude)
potholes = [
    {"lat": 13.0827, "lng": 80.2707, "severity": "High"},
    {"lat": 13.0604, "lng": 80.2496, "severity": "Medium"}
]

@app.route('/')
def index():
    # Renders the frontend HTML file
    return render_template('index.html')

@app.route('/api/potholes')
def get_potholes():
    # Sends pothole data to the frontend
    return jsonify(potholes)

@app.route('/api/predict_traffic/<time>')
def predict_traffic(time):
    # In a real app, you would use pandas here to load a CSV model
    # df = pd.read_csv('traffic_data.csv')
    # logic to predict traffic based on 'time' parameter
    
    # Simulating a traffic status for the prototype
    statuses = ["Green", "Neutral", "Red"]
    return jsonify({"predicted_status": random.choice(statuses)})

if __name__ == '__main__':
    app.run(debug=True)
