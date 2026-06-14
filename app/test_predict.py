
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_predict():

    payload = {

        "recency_days":120,
        "frequency_180d":1,
        "monetary_180d":900,
        "ticket_count_90d":5,
        "sessions_30d":1

    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "churn_probability" in data

    assert "predicted_class" in data

    assert "risk_level" in data
