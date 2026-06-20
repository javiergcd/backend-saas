from fastapi.testclient import TestClient

#from app.main import app

from fastapi import FastAPI
app = FastAPI()

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200 
