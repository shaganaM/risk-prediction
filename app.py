from flask import Flask, request, jsonify
from model import predict_risk

app = Flask(__name__)

@app.route('/')
def home():
    return "Cardiac Arrest Risk Prediction System"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    blood_sugar = data.get('blood_sugar')
    bp = data.get('bp')
    ckmb = data.get('ckmb')
    troponin = data.get('troponin')

    result = predict_risk(blood_sugar, bp, ckmb, troponin)

    return jsonify({"Risk Level": result})

if __name__ == '__main__':
    app.run(debug=True)
