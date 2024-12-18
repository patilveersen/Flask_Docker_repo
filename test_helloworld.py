import pytest
from helloworld import app


# proxy to a live server.
@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    resp = client.get("/")
    assert resp.status_code == 444
