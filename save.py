import joblib

def load_model():
    model = joblib.load('model.pkl')
    label_encoder = joblib.load('label_encoder.pkl')
    return model, label_encoder
