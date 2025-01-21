import pytest
from main import create_app
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_payment_creation(client):
    response = client.post("/api/v1/payments", json = {
        "customer_name": "Braddy White",
        "customer_email": "braddy@example.com",
        "amount": 80.00
    },
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    })
    assert response.status_code == 201
    assert response.json["status"] == "success"


def test_payment_status(client):
    response = client.post("/api/v1/payments", json={
        "customer_name": "Luke Stones",
        "customer_email": "luke@example.com",
        "amount": 200.00
    },
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    })
    
    payment_id = response.json["payment"]["id"]

    status_response = client.get(f"/api/v1/payments/{payment_id}", headers = {
        "Authorization": f"Bearer {API_KEY}"
    })
   
    assert status_response.status_code == 200
    assert status_response.json["payment"]["status"] in ["pending", "abandoned"]