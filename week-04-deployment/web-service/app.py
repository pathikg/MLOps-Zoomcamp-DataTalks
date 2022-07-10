from flask import Flask, request, jsonify
from utils import *

# define our app
app = Flask("nyc-taxi-duration")

# /predict-duration endpoint to talk with our API
@app.route("/predict-duration", methods=["GET"])
def predict_duration(request):
    """Returns JSON response of predicted duration for the data obtained from the body of incoming request"""
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features)

    result = {"duration": pred}
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
