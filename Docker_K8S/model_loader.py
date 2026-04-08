import xgboost as xgb
import os

MODEL_PATH = "xgboost-model"

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

    model = xgb.Booster()
    model.load_model(MODEL_PATH)
    return model
