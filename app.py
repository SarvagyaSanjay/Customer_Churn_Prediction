import os
import pickle
import numpy as np
import pandas as pd
from flask import Flask,jsonify, request, render_template

# ── App Setup ────────────────────────────────────────────────────────────────
app = Flask(__name__, template_folder="templates")

# ── Load Model & Scaler ───────────────────────────────────────────────────────
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(MODEL_PATH, "rb") as f:
    artifacts = pickle.load(f)

model  = artifacts["model"]
scaler = artifacts["scaler"]

# ── Feature columns (must match training order exactly) ──────────────────────
FEATURE_COLS = [
    "SeniorCitizen", "tenure", "MonthlyCharges", "TotalCharges",
    "gender_Male", "Partner_Yes", "Dependents_Yes", "PhoneService_Yes",
    "MultipleLines_No phone service", "MultipleLines_Yes",
    "InternetService_Fiber optic", "InternetService_No",
    "OnlineSecurity_No internet service", "OnlineSecurity_Yes",
    "OnlineBackup_No internet service", "OnlineBackup_Yes",
    "DeviceProtection_No internet service", "DeviceProtection_Yes",
    "TechSupport_No internet service", "TechSupport_Yes",
    "StreamingTV_No internet service", "StreamingTV_Yes",
    "StreamingMovies_No internet service", "StreamingMovies_Yes",
    "Contract_One year", "Contract_Two year",
    "PaperlessBilling_Yes",
    "PaymentMethod_Credit card (automatic)",
    "PaymentMethod_Electronic check",
    "PaymentMethod_Mailed check",
]


def encode_form(form) -> np.ndarray:
    """Convert raw HTML form data into the scaled feature array the model expects."""

    # --- raw values ---
    senior        = int(form["SeniorCitizen"])
    tenure        = float(form["tenure"])
    monthly       = float(form["MonthlyCharges"])
    total         = float(form["TotalCharges"])
    gender        = form["gender"]
    partner       = form["Partner"]
    dependents    = form["Dependents"]
    phone         = form["PhoneService"]
    multi         = form["MultipleLines"]
    internet      = form["InternetService"]
    online_sec    = form["OnlineSecurity"]
    online_bkp    = form["OnlineBackup"]
    device_prot   = form["DeviceProtection"]
    tech_sup      = form["TechSupport"]
    stream_tv     = form["StreamingTV"]
    stream_mv     = form["StreamingMovies"]
    contract      = form["Contract"]
    paperless     = form["PaperlessBilling"]
    payment       = form["PaymentMethod"]

    # --- one-hot encode (drop_first=True mirrors training) ---
    row = {col: 0 for col in FEATURE_COLS}

    row["SeniorCitizen"]   = senior
    row["tenure"]          = tenure
    row["MonthlyCharges"]  = monthly
    row["TotalCharges"]    = total

    if gender == "Male":
        row["gender_Male"] = 1
    if partner == "Yes":
        row["Partner_Yes"] = 1
    if dependents == "Yes":
        row["Dependents_Yes"] = 1
    if phone == "Yes":
        row["PhoneService_Yes"] = 1

    if multi == "No phone service":
        row["MultipleLines_No phone service"] = 1
    elif multi == "Yes":
        row["MultipleLines_Yes"] = 1

    if internet == "Fiber optic":
        row["InternetService_Fiber optic"] = 1
    elif internet == "No":
        row["InternetService_No"] = 1

    if online_sec == "No internet service":
        row["OnlineSecurity_No internet service"] = 1
    elif online_sec == "Yes":
        row["OnlineSecurity_Yes"] = 1

    if online_bkp == "No internet service":
        row["OnlineBackup_No internet service"] = 1
    elif online_bkp == "Yes":
        row["OnlineBackup_Yes"] = 1

    if device_prot == "No internet service":
        row["DeviceProtection_No internet service"] = 1
    elif device_prot == "Yes":
        row["DeviceProtection_Yes"] = 1

    if tech_sup == "No internet service":
        row["TechSupport_No internet service"] = 1
    elif tech_sup == "Yes":
        row["TechSupport_Yes"] = 1

    if stream_tv == "No internet service":
        row["StreamingTV_No internet service"] = 1
    elif stream_tv == "Yes":
        row["StreamingTV_Yes"] = 1

    if stream_mv == "No internet service":
        row["StreamingMovies_No internet service"] = 1
    elif stream_mv == "Yes":
        row["StreamingMovies_Yes"] = 1

    if contract == "One year":
        row["Contract_One year"] = 1
    elif contract == "Two year":
        row["Contract_Two year"] = 1

    if paperless == "Yes":
        row["PaperlessBilling_Yes"] = 1

    if payment == "Credit card (automatic)":
        row["PaymentMethod_Credit card (automatic)"] = 1
    elif payment == "Electronic check":
        row["PaymentMethod_Electronic check"] = 1
    elif payment == "Mailed check":
        row["PaymentMethod_Mailed check"] = 1

    # Build DataFrame in training column order, then scale
    df_input = pd.DataFrame([row], columns=FEATURE_COLS)
    scaled   = scaler.transform(df_input)
    return scaled


# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = encode_form(request.form)
        pred     = model.predict(features)[0]
        result   = "Yes" if pred == 1 else "No"
    except Exception as e:
        result = f"Error: {e}"

    return render_template("index.html", prediction=result)


# ── Entry Point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

# if __name__=="__main__":
#     app.run(debug=True)