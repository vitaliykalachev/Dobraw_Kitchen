from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_root():
    res = client.get("/")
    print(res.json().get('Hello'))
    assert res.json().get('Hello') == "Привет, как дела, заходи в гости"
    assert res.status_code == 200