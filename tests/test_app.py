import json
import pytest
from app import app


@pytest.fixture()
def client():
    app.testing = True
    with app.test_client() as c:
        yield c


def test_root(client):
    rv = client.get("/")
    assert rv.status_code == 200
    data = rv.get_json()
    assert data.get("ok") is True


def test_echo(client):
    rv = client.get("/echo?msg=hi")
    assert rv.status_code == 200
    assert rv.get_json()["echo"] == "hi"


def test_validate_ok(client):
    rv = client.post("/validate", data=json.dumps({"message": "x", "count": 2}), content_type="application/json")
    assert rv.status_code == 200
    assert rv.get_json()["ok"] is True


def test_validate_bad(client):
    rv = client.post("/validate", data=json.dumps({"message": "", "count": 0}), content_type="application/json")
    assert rv.status_code == 400
    assert rv.get_json()["ok"] is False
