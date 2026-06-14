
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_invalid_input():

    payload = {

        "recency_days":-10,
        "frequency_180d":1,
        "monetary_180d":500,
        "ticket_count_90d":1,
        "sessions_30d":2

    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 422
