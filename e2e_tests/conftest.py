import subprocess
import time

import pytest
import requests


@pytest.fixture(scope="session", autouse=True)
def django_server():
    # Start containers
    # pylint: disable-next=consider-using-with
    server_process = subprocess.Popen(["e2e_tests/run_servers.sh"], stdin=subprocess.PIPE)

    # Wait 60 seconds for the server to be ready
    max_retries = 60
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get("http://localhost:8000/") # pylint: disable=missing-timeout
            if response.status_code == 200:
                break
        except requests.ConnectionError:
            pass

        retries += 1
        time.sleep(1)

    # Run tests
    yield

    # Stop containers and remove data
    server_process.communicate(input=b'q')
