from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS,cross_origin


app = Flask(__name__)
CORS(app,supports_credentials=True)

@app.route('/predict', methods=['POST','OPTIONS'])
@cross_origin()

def predict():
    if request.method == 'OPTIONS':
        headers={
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            
            
        }
        return '',204,headers
    model=joblib.load('model.pkl')
    label_encoder=joblib.load('label_encoder.pkl')
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
        return jsonify({'error': f"Invalid data type: {e}"}), 400
    try:
        x_new = np.array([[temperature, precipitation, humidity]])
        prediction = model.predict(x_new)[0]
        weather=label_encoder.inverse_transform([prediction])[0]
    except Exception as e:
        return jsonify({'error': f"Failed to make prediction: {e}"}), 500
    return jsonify({'Weather Condition': weather}),200

if __name__ == '__main__':
    app.run(port=5000,debug=True)