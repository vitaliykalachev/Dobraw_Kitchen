import pytest
from jose import jwt
from app import schemas
from .database import client, session
from app.config import settings


@pytest.fixture
def test_user(client):
    user_data = {"email": "vit@gmail.com",
                 "password": "password123"}
    
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201
    print(res.json())
    new_user = res.json()
    new_user['password'] = user_data['password']
    
    return new_user



# def test_root(client):
    
#     res = client.get("/")
#     print(res.json().get('Hello'))
#     assert res.json().get('Hello') == "Привет, как дела, заходи в гости"
#     assert res.status_code == 200
    
def test_create_user(client):
    res = client.post("/users/", json={"email": "hello123@gmail.com", "password": "password123"})
    print(res.json())
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201
    
def test_login_user(test_user, client):
    res = client.post(
        "/login", data={"username": test_user['email'], "password": test_user["password"]})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200