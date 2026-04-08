from flask import Flask, request, jsonify
import numpy as np
import xgboost as xgb
from model_loader import load_model

app = Flask(__name__)

# Load model at startup
model = load_model()

@app.route("/")
def home():
    return {"message": "XGBoost Model API Running"}

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Input validation
        cgpa = float(data["cgpa"])
        iq = int(data["iq"])
        profile_score = int(data["profile_score"])

        # Convert to DMatrix
        features = np.array([[cgpa, iq, profile_score]])
        dmatrix = xgb.DMatrix(features)

        prediction = model.predict(dmatrix)

        return jsonify({
            "prediction": float(prediction[0])
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    # For local testing only (not used in Docker)
    app.run(host="0.0.0.0", port=5000)
