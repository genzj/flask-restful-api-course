from meal_options import create_app

import pytest


@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    # set up here
    yield app
    # tear down here


@pytest.fixture
def client(app):
    return app.test_client()


def test_index(client):
    response = client.get("/")
    assert response.status != 500
