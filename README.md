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

## Business Objective

The goal is to help the business identify customers at risk of churn before they leave and support targeted retention interventions.

This API serves as a scoring layer that can be integrated into internal CRM systems.

---

## Repository Structure

```text
Project_Part-4/

├── app.py
├── train_model.py
├── model.pkl
├── rfm_modeling_snapshot.csv

├── requirements.txt
├── README.md

├── monitoring_plan.md
├── responsible_use.md

├── test_health.py
├── test_predict.py
├── test_batch_predict.py
├── test_invalid_input.py

├── outputs/
│   ├── swagger_home.png
│   ├── health_response.png
│   ├── predict_response.png
│   ├── batch_predict_response.png
│   ├── predict_response.json
│   └── batch_predict_response.json
```

---

## Source Dataset

Model training data:

* rfm_modeling_snapshot.csv

Target variable:

* churn_next_60d

Important Leakage Prevention:

Only information available on or before the customer snapshot date is used for model training.

No post-snapshot information is used as model input.

This complies with the capstone leakage-prevention requirements.

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
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Documentation

Swagger UI provides interactive documentation for:

* GET /health
* POST /predict
* POST /batch_predict

All endpoints support request validation through Pydantic models.

---

## Endpoint Details

### GET /health

Health-check endpoint.

Example Response:

```json
{
  "status": "ok"
}
```

---

### POST /predict

Predict churn risk for a single customer.

Example Request:

```json
{
  "recency_days": 120,
  "frequency_180d": 2,
  "monetary_180d": 1500,
  "ticket_count_90d": 4,
  "sessions_30d": 1
}
```

Example Response:

```json
{
  "churn_probability": 0.81,
  "predicted_class": 1,
  "risk_level": "high",
  "risk_explanation": "inactive customer, high complaint volume, low engagement"
}
```

---

### POST /batch_predict

Predict churn risk for multiple customers.

Example Request:

```json
{
  "customers": [
    {
      "recency_days": 120,
      "frequency_180d": 2,
      "monetary_180d": 1500,
      "ticket_count_90d": 4,
      "sessions_30d": 1
    },
    {
      "recency_days": 10,
      "frequency_180d": 8,
      "monetary_180d": 9000,
      "ticket_count_90d": 0,
      "sessions_30d": 12
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

## API Execution Evidence

The outputs folder contains:

* swagger_home.png
* health_response.png
* predict_response.png
* batch_predict_response.png

These screenshots demonstrate successful execution of the API endpoints.

JSON response examples are also included:

* predict_response.json
* batch_predict_response.json

These files provide evidence that the API was executed successfully and returned valid prediction responses.

---

## Monitoring

See:

```text
monitoring_plan.md
```

The monitoring plan covers:

* Data drift
* Prediction distribution drift
* API failures and latency
* Business outcomes
* Retraining triggers

---

## Responsible Use

See:

```text
responsible_use.md
```

The model should only be used to support customer-retention activities.

The model should NOT be used for:

* Credit decisions
* Employment decisions
* Legal decisions
* Service denial
* Customer discrimination

Predictions should support human decision-making rather than replace it.

---

## Reproducibility

The repository includes:

* Source data
* Model training script
* Saved model artifact
* API code
* Automated tests
* Requirements file

A reviewer can reproduce the workflow by:

```bash
pip install -r requirements.txt
python train_model.py
uvicorn app:app --reload
```

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

---

## Author Notes

This project was developed as Part 4 of the D2C Customer Churn Intelligence & Retention API Capstone Project.

The API exposes machine-learning churn predictions in a format suitable for CRM integration and retention decision support.
