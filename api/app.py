from flask import Flask, request, jsonify
import numpy as np
from save import load_model  #to load your model
from flask_cors import CORS

app = Flask(__name__)
CORS(app,origins="*")

# Load the model and label encoder
model, label_encoder = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Failed to load model'}), 500
    
    try:
        data = request.get_json(force=True)
        temperature = data['Temperature']
        precipitation = data['Precipitation']
        humidity = data['Humidity']
    except KeyError as e:
        return jsonify({'error': f"Missing required field: {e}"}), 400
    except TypeError as e:
        return jsonify({'error': f"Invalid data format: {e}"}), 400

    try:
        x_new = np.array([[temperature, precipitation, humidity]])
        prediction = model.predict(x_new)[0]
        weather_condition = label_encoder.inverse_transform([prediction])[0]
    except Exception as e:
        return jsonify({'error': f"Prediction error: {e}"}), 500

    return jsonify({'Weather Condition': weather_condition})

if __name__ == '__main__':
    app.run(debug=True)
