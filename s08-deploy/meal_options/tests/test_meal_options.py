from flask import Flask
from flask.testing import FlaskClient
from meal_options import create_app
from typing import Generator

import pytest


@pytest.fixture
def app() -> Generator[Flask, None, None]:
    app = create_app({
        "TESTING": True,
        "TOKEN_TO_USER_MAPPING": {
            "unittest-token": "unittest",
        },
    })
    # set up here
    yield app
    # tear down here


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def test_no_login(client: FlaskClient):
    response = client.get("/meals")
    assert response.status_code == 403


def test_correct_login(client: FlaskClient):
    headers = {
        "USER_TOKEN": "unittest-token",
    }
    response = client.get("/meals", headers=headers)
    assert response.status_code == 200
