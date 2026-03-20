from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from model import predict_premium, detect_fraud

app = Flask(__name__)
CORS(app)

# Home -> Login page
@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Premium prediction
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    hours = int(data["hours"])
    risk = int(data["risk"])
    weather = int(data["weather"])
    claims = int(data["claims"])

    premium = predict_premium(hours, risk, weather, claims)

    return jsonify({"premium": premium})


# Calculate premium
@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json

    name = data["name"]
    hours = int(data["hours"])
    risk = int(data["risk"])
    claims = int(data["claims"])
    weather = int(data["weather"])

    premium = (hours * 2) + (risk * 10) + (claims * 20) + (weather * 15)

    fraud = detect_fraud(hours, risk, claims, weather)

    return jsonify({
        "name": name,
        "premium": premium,
        "fraud": fraud
    })


if __name__ == "__main__":
    app.run(debug=True)