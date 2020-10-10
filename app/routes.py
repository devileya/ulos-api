from app import app
from app.controller import PredictController


@app.route("/predict", methods=["POST"])
def predict():
    return PredictController.prediction()
