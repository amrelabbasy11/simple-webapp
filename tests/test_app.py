from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_hello():
    client = app.test_client()
    response = client.get("/how are you")
    assert response.status_code == 200
    