from app import schemas
from .database import client, session



def test_root(client):
    
    res = client.get("/")
    print(res.json().get('Hello'))
    assert res.json().get('Hello') == "Привет, как дела, заходи в гости"
    assert res.status_code == 200
    
def test_create_user(client):
    res = client.post("/users/", json={"email": "hello123@gmail.com", "password": "password123"})
    print(res.json())
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201
    
def test_login_user(client):
    res = client.post(
        "/login", data={"username": "hello123@gmail.com", "password": "password123"})
    print(res.json())
    assert res.status_code == 200