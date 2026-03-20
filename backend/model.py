import numpy as np
from sklearn.linear_model import LinearRegression

# Dummy training data
X = np.array([
    [5,2,0,1],
    [8,5,1,2],
    [10,7,0,3],
    [3,1,1,0],
    [6,4,0,2]
])

y = np.array([50,120,180,30,90])

# Train model
model = LinearRegression()
model.fit(X,y)

# ---------------- PREDICT PREMIUM ----------------

def predict_premium(hours, city_risk, rain, claims):

    data = np.array([[hours, city_risk, rain, claims]])
    premium = model.predict(data)[0]

    if premium < 0:
        premium = 0

    return round(premium,2)


# ---------------- FRAUD DETECTION ----------------

def detect_fraud(hours, risk, claims, weather):

    if claims > 5 and risk > 7:
        return "High Risk Fraud"

    elif claims > 3:
        return "Medium Risk"

    else:
        return "Low Risk"