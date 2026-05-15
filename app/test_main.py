# app/test_main.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_tools_empty():
    # Test hitting the GET endpoint when database is empty/starting up
    response = client.get("/tools/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)