from flask import Flask, request, jsonify
from utils import *

# define our app
app = Flask("nyc-taxi-duration")

dv, model = load_model("lin_reg.bin")

# /predict-duration endpoint to talk with our API
@app.route("/predict-duration", methods=["GET"])
def predict_duration():
    """Returns JSON response of predicted duration for the data obtained from the body of incoming request"""
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features, dv, model)

    result = {"duration": pred}
    return jsonify(result)