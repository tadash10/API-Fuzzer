import requests

def test_authentication(api_endpoint, valid_credentials, invalid_credentials):
    try:
        valid_response = requests.get(api_endpoint, auth=valid_credentials, timeout=5)
        invalid_response = requests.get(api_endpoint, auth=invalid_credentials, timeout=5)

        if valid_response.status_code == 200:
            return "Authentication with valid credentials successful."
        elif invalid_response.status_code == 401:
            return "Authentication with invalid credentials failed (expected behavior)."
        else:
            return "Authentication test failed due to an unexpected response."
    except requests.exceptions.RequestException as e:
        return f"Authentication test failed with an exception: {str(e)}"
