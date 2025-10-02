# src/test/test_hello.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hello import lambda_handler

def test_lambda_returns_hello_world():
    response = lambda_handler({}, {})
    assert response['body'] == 'Hello World'
