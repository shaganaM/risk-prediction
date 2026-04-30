def predict_risk(blood_sugar, bp, ckmb, troponin):
    if troponin > 0.4 or ckmb > 25:
        return "High Risk"
    elif blood_sugar > 180 or bp > 140:
        return "Medium Risk"
    else:
        return "Low Risk"
