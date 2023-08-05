from fastapi.testclient import TestClient
from main import app
from fastapi import status
from main import predict

client=TestClient(app=app)

def test_predict_sick():
    payload={
        
        
        "gravity": 1.007,
        "ph": 6.63,
        "cond": 8.4,
        "calc": 2.4,
        "osmo": 100,
        "urea":10
    }

    response=client.post("/predict",json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] == "Patient has kidney stone"


def test_predict_negative():
    payload={
        
        
        "gravity": 1.007,
        "ph": 6.63,
        "cond": 8.4,
        "calc": 2.1,
        "osmo": 100,
        "urea":10
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] == "Patient has not kidney stone"

def test_predict_invalid():
    payload={
        "gravity": 1.007,
        "ph": 6.63,
        "cond": 8.4,
        "calc": 2.1,
        "osmo": "invalid",
        "urea":10
    } 
    response = client.post("/predict", json=payload)

    assert response.status_code == 422
    assert "detail" in response.json()   


#success
"""{
  "gravity": 1.007,
  "ph": 6.63,
  "cond": 8.4,
  "calc": 2.4,
  "osmo": 100,
  "urea":10
}
"""
#failure
"""{
  "gravity": 1.007,
  "ph": 6.63,
  "cond": 8.4,
  "calc": 2.1,
  "osmo": 100,
  "urea":10
}
"""


