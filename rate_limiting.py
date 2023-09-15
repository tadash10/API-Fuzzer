import time
import requests

def test_rate_limiting(api_endpoint, num_requests, delay_seconds):
    try:
        detected_limiting = False
        for _ in range(num_requests):
            response = requests.get(api_endpoint, timeout=5)
            if response.status_code == 429:
                detected_limiting = True
                break
            time.sleep(delay_seconds)

        if detected_limiting:
            return f"Rate limiting detected after {_} requests."
        else:
            return f"No rate limiting detected for {num_requests} requests with {delay_seconds} seconds delay."
    except requests.exceptions.RequestException as e:
        return f"Rate limiting testing failed with an exception: {str(e)}"
