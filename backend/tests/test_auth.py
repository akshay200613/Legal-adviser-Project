from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to AI Legal Adviser API", "docs": "/docs"}

def test_login():
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "admin@example.com", "password": "admin"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_fail():
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "admin@example.com", "password": "wrongpassword"}
    )
    assert response.status_code == 400
