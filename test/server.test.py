import pytest
import server

# Ensure the test server is always shut down after the test module runs
@pytest.fixture(scope="module", autouse=True)
def close_server():
    yield
    server.close()

# Existing test(s) – the server is started inside the test and will be closed by the fixture

def test_server():
    server.start()
    assert server.is_running()
