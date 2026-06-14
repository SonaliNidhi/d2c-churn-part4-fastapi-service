
from fastapi import FastAPI

from app.schemas import (
    CustomerRequest,
    BatchRequest
)

from app.risk_engine import (
    risk_reason
)

import pandas as pd
import joblib

app = FastAPI(
    title="D2C Churn API"
)

model = joblib.load(
    "model.pkl"
)

@app.get("/health")
def health():

    return {
        "status": "ok"
    }

@app.post("/predict")
def predict(
    customer: CustomerRequest
):

    data = pd.DataFrame([{

        "recency_days":
        customer.recency_days,

        "frequency_180d":
        customer.frequency_180d,

        "monetary_180d":
        customer.monetary_180d,

        "ticket_count_90d":
        customer.ticket_count_90d,

        "sessions_30d":
        customer.sessions_30d

    }])

    probability = float(

        model.predict_proba(
            data
        )[0][1]

    )

    prediction = int(
        probability >= 0.40
    )

    if probability >= 0.70:

        level = "high"

    elif probability >= 0.40:

        level = "medium"

    else:

        level = "low"

    return {

        "churn_probability":
        round(probability, 4),

        "predicted_class":
        prediction,

        "risk_level":
        level,

        "risk_explanation":
        risk_reason(customer)

    }

@app.post("/batch_predict")
def batch_predict(
    request: BatchRequest
):

    results = []

    for customer in request.customers:

        results.append(
            predict(customer)
        )

    return {

        "predictions":
        results

    }
