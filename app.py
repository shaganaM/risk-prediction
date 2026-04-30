from flask import Flask, request, jsonify

app = Flask(__name__)

def predict_risk(marks, attendance):
    if marks > 75 and attendance > 75:
        return "Low Risk"
    elif marks > 50:
        return "Medium Risk"
    else:
        return "High Risk"

@app.route('/')
def home():
    return "Student Risk Prediction System"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    marks = data.get('marks')
    attendance = data.get('attendance')

    result = predict_risk(marks, attendance)
    return jsonify({"Risk Level": result})

if __name__ == '__main__':
    app.run(debug=True)
