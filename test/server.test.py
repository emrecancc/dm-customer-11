import subprocess
import time
import requests
import socket

# Helper to find an unused TCP port
def _get_free_port():
    s = socket.socket()
    s.bind(("", 0))
    _, port = s.getsockname()
    s.close()
    return port

# Test that a simple HTTP server can be started and responds correctly
# The server is started on a random free port to avoid port conflicts
# and is guaranteed to be shut down after the test, preventing flaky
# failures caused by a previously running server.

def test_server():
    port = _get_free_port()
    server = subprocess.Popen(["python", "-m", "http.server", str(port)])
    try:
        # Give the server a moment to start up
        time.sleep(1)
        response = requests.get(f"http://localhost:{port}")
        assert response.status_code == 200
    finally:
        # Ensure the server process is terminated regardless of test outcome
        server.terminate()
        server.wait()
