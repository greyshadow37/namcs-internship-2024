import joblib

def load_model():
    model = joblib.load('../model/model.pkl')
    label_encoder = joblib.load('../model/label_encoder.pkl')
    return model, label_encoder
