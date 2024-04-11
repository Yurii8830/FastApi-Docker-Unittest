import pytest
from fastapi.testclient import TestClient
from main import app
from sqlalchemy.orm import Session
from database import get_db, engine
from dto import user as UserDTO, record as RecordDTO
from models.user import User
from models.record import Record
from services import user as UserService, record as RecordService

# Create a test client using TestClient from FastAPI
@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

# Create a test database session
@pytest.fixture(scope="module")
def test_db():
    connection = engine.connect()
    transaction = connection.begin()
    yield session
    transaction.rollback()
    connection.close()

# Override the dependency for database with the test database session
@pytest.fixture
def override_get_db(test_db):
    yield test_db

# Test cases for the endpoints
def test_create_user(client, override_get_db):
    data = UserDTO.User(name="Test User", email="test@example.com", age=30, is_active=True, registration_date="2024-04-15")
    response = client.post("/user", json=data.dict())
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"

def test_read_user(client, override_get_db):
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"

def test_update_user(client, override_get_db):
    data = UserDTO.User(name="Updated User", email="updated@example.com", age=40, is_active=False, registration_date="2024-04-16")
    response = client.put("/user/1", json=data.dict())
    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"

def test_delete_user(client, override_get_db):
    response = client.delete("/user/1")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted successfully"

def test_create_record(client, override_get_db):
    user_data = UserDTO.User(name="Test User", email="test@example.com", age=30, is_active=True, registration_date="2024-04-15")
    user = UserService.create_user(user_data, override_get_db)
    record_data = RecordDTO.Record(title="Test Record", content="Test Content", user_id=user.id)
    response = client.post("/record", json=record_data.dict())
    assert response.status_code == 200
    assert response.json()["title"] == "Test Record"

def test_read_record(client, override_get_db):
    response = client.get("/record/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Record"

def test_update_record(client, override_get_db):
    data = RecordDTO.Record(title="Updated Record", content="Updated Content")
    response = client.put("/record/1", json=data.dict())
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Record"

def test_delete_record(client, override_get_db):
    response = client.delete("/record/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Record deleted successfully"
