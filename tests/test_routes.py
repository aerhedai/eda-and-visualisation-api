import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def sample_dataset():
    return {
        "rows": [
            {"age": 25, "income": 50000, "gender": "Male"},
            {"age": 30, "income": 60000, "gender": "Female"},
            {"age": 22, "income": None, "gender": "Male"}
        ]
    }

def test_eda_insights(sample_dataset):
    response = client.post("/eda-insights", json=sample_dataset)
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert isinstance(data["summary"], dict)
    assert "missing_values" in data["summary"]

def test_visualisation(sample_dataset):
    response = client.post("/visualisation", json=sample_dataset)
    assert response.status_code == 200
    data = response.json()
    assert "charts" in data
    assert isinstance(data["charts"], list)
    for chart in data["charts"]:
        assert "type" in chart
        assert "data" in chart
