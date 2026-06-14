from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

import pandas as pd
import joblib

model = joblib.load(
    "model.pkl"
)

app = FastAPI(
    title="D2C Customer Churn API"
)

class CustomerRequest(BaseModel):

    recency_days: int = Field(..., ge=0)

    frequency_180d: int = Field(..., ge=0)

    monetary_180d: float = Field(..., ge=0)

    ticket_count_90d: int = Field(..., ge=0)

    sessions_30d: int = Field(..., ge=0)

class BatchRequest(BaseModel):

    customers: list[CustomerRequest]

def risk_reason(customer):

    reasons = []

    if customer.recency_days > 90:
        reasons.append("high inactivity")

    if customer.ticket_count_90d > 3:
        reasons.append("multiple complaints")

    if customer.sessions_30d < 3:
        reasons.append("low engagement")

    if customer.frequency_180d < 2:
        reasons.append("low purchase frequency")

    if not reasons:
        reasons.append("healthy customer behavior")

    return ", ".join(reasons)

@app.get("/health")
def health():

    return {

        "status": "ok"

    }

@app.post("/predict")
def predict(customer: CustomerRequest):

    try:

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
            model.predict_proba(data)[0][1]
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

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@app.post("/batch_predict")
def batch_predict(
    request: BatchRequest
):

    predictions = []

    for customer in request.customers:

        predictions.append(
            predict(customer)
        )

    return {

        "predictions":
        predictions

    }
