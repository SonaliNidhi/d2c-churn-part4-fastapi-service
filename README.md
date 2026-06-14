# D2C Customer Churn Intelligence API

## Project Overview

This project exposes churn-risk predictions through a FastAPI service for use by CRM, retention, marketing, and customer-success teams.

The API uses a machine-learning model trained on customer behavioral features from the D2C Customer Churn Intelligence dataset.

The service returns:

* Churn probability
* Predicted churn class
* Risk level
* Risk explanation

---

## Repository Structure

```text
app.py
train_model.py
model.pkl

requirements.txt

monitoring_plan.md
responsible_use.md

test_health.py
test_predict.py
test_batch_predict.py
test_invalid_input.py
```

---

## Source Dataset

Model training data:

* rfm_modeling_snapshot.csv

Target variable:

* churn_next_60d

Only information available on or before the customer snapshot date is used for model training.

No post-snapshot information is used as model input.

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Train Model

```bash
python train_model.py
```

This generates:

```text
model.pkl
```

---

## Run API

```bash
uvicorn app:app --reload
```

API available at:

```text
https://jacket-upbeat-abreast.ngrok-free.dev/docs
```

Swagger documentation:

```text
https://jacket-upbeat-abreast.ngrok-free.dev/docs```
---

## Endpoint Details

### GET /health

Health-check endpoint.

Example Response:

```json
{
    "status":"ok"
}
```

---

### POST /predict

Predict churn risk for a single customer.

Example Request:

```json
{
    "recency_days":120,
    "frequency_180d":2,
    "monetary_180d":1500,
    "ticket_count_90d":4,
    "sessions_30d":1
}
```

Example Response:

```json
{
    "churn_probability":0.81,
    "predicted_class":1,
    "risk_level":"high",
    "risk_explanation":"high inactivity, multiple complaints, low engagement"
}
```

---

### POST /batch_predict

Predict churn risk for multiple customers.

Example Request:

```json
{
    "customers":[
        {
            "recency_days":120,
            "frequency_180d":2,
            "monetary_180d":1500,
            "ticket_count_90d":4,
            "sessions_30d":1
        },
        {
            "recency_days":10,
            "frequency_180d":8,
            "monetary_180d":9000,
            "ticket_count_90d":0,
            "sessions_30d":12
        }
    ]
}
```

---

## Run Tests

```bash
pytest
```

Included Tests:

* test_health.py
* test_predict.py
* test_batch_predict.py
* test_invalid_input.py

---

## Monitoring

See:

```text
monitoring_plan.md
```

The monitoring plan covers:

* Data drift
* Prediction drift
* API errors
* Business outcomes
* Retraining triggers

---

## Responsible Use

See:

```text
responsible_use.md
```

The model should only be used to support retention campaigns.

The model should not be used for:

* Credit decisions
* Employment decisions
* Legal decisions
* Service denial

Human review is recommended before taking action on high-risk predictions.

---

## Docker (Optional)

Build Image:

```bash
docker build -t churn-api .
```

Run Container:

```bash
docker run -p 8000:8000 churn-api
```
