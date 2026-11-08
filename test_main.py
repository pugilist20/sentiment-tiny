from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_positive():
    response = client.post(
        "/predict",
        json={"text": "this mod is sooo good"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["label"] in ("POSITIVE", "NEGATIVE")
    assert 0 <= data["score"] <= 1


def test_predict_returns_label():
    response = client.post(
        "/predict",
        json={"text": "it wouldn't import, it's broken"}
    )
    assert response.status_code == 200
    assert "label" in response.json()