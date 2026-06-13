from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "AI Resume Matcher API is running"


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_model_info_endpoint():
    response = client.get("/model-info")
    assert response.status_code == 200
    assert response.json()["model"] == "RandomForestClassifier"
    assert response.json()["task"] == "Resume suitability prediction"