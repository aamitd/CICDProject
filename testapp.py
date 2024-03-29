import os
import pytest
from pymongo import MongoClient
from main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    # Test if the response for the main route is 200 (OK)
    rv = client.get('/')
    assert rv.status_code == 200
