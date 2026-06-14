
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_batch():

    payload = {

        "customers":[

            {

                "recency_days":120,
                "frequency_180d":1,
                "monetary_180d":800,
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

    response = client.post(
        "/batch_predict",
        json=payload
    )

    assert response.status_code == 200

    assert "predictions" in response.json()
