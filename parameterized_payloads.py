import requests

def test_parameterized_payload(api_endpoint, param_name, payloads):
    try:
        for payload in payloads:
            params = {param_name: payload}
            response = requests.get(api_endpoint, params=params, timeout=5)

            if 'error' in response.text.lower():
                return f"Potential vulnerability found with payload: {payload}"

        return "No vulnerabilities found with parameterized payloads."
    except requests.exceptions.RequestException as e:
        return f"Payload testing failed with an exception: {str(e)}"
