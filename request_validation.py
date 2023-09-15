import requests

def test_request_validation(api_endpoint, payloads):
    try:
        results = []
        for payload in payloads:
            response = requests.post(api_endpoint, data=payload, timeout=5)

            if response.status_code != 200:
                results.append(f"Potential vulnerability found with payload: {payload}")
        
        if not results:
            return "No vulnerabilities found with request validation testing."
        
        return "\n".join(results)
    except requests.exceptions.RequestException as e:
        return f"Request validation testing failed with an exception: {str(e)}"
