import pytest
import requests
import json

from wiremock.testing.testcontainer import wiremock_container
from wiremock.constants import Config
from wiremock.client import *

@pytest.fixture # (1)
def wiremock_server():
    with wiremock_container(secure=False) as wm:
        Config.base_url = wm.get_url("__admin") # (2)  
        yield wm

def test_count_number_of_element_in_response(wiremock_server): # (4)
    response = requests.get(("http://localhost:8080/users"))

    assert response.status_code == 200
    print(response.json())
    assert len(response.json()) == 2