from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS


app = Flask(__name__)
CORS(app,origins="*")

@app.route('/predict', methods=['POST'])
def predict():
    model=joblib.load('model.py')
    if model is None:
        return jsonify({'error': 'Failed to load model'}), 500
    try:
        data = request.get_json()
        temperature = data['Temperature']
        precipitation = data['Precipitation']
        humidity = data['Humidity']
    except KeyError as e:
        return jsonify({'error': f"Missing required field: {e}"}), 400
    x_new = np.array([[temperature, precipitation, humidity]])
    prediction = model.predict(x_new)[0]
    return jsonify({'Weather Condition': prediction})

if __name__ == '__main__':
    app.run(debug=True)