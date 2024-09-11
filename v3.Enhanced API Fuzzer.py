import requests
import argparse
import logging

# Define default payloads and endpoints
DEFAULT_API_ENDPOINTS = [
    "/api/v1/login",
    "/api/v1/user",
    "/api/v1/products",
    "/api/v1/orders",
]

DEFAULT_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "1' OR '1'='1",
    "SELECT * FROM users;",
    "<img src=x onerror=alert('XSS')>",
    "' OR '1'='1' --",
    "<script>console.log('XSS')</script>",
]

# Setup logging
logging.basicConfig(filename='api_fuzzer.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def api_fuzzer(base_url, endpoints, payloads):
    for endpoint in endpoints:
        for payload in payloads:
            url = base_url + endpoint
            headers = {"Content-Type": "application/json"}
            data = {"param": payload}

            try:
                response = requests.post(url, json=data, headers=headers)
                # Improved response checks
                if response.status_code == 200:
                    if any(err in response.text.lower() for err in ["error", "exception", "failed"]):
                        logging.info(f"Potential vulnerability found at {url} with payload: {payload}")
                    else:
                        logging.info(f"Successful response at {url} with payload: {payload}")
                else:
                    logging.info(f"Non-200 status code {response.status_code} at {url} with payload: {payload}")

            except requests.exceptions.RequestException as e:
                logging.error(f"Error with {url} and payload {payload}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="API Fuzzer - Security Testing Tool")
    parser.add_argument('base_url', type=str, help='Base URL of the API to be tested')
    parser.add_argument('--endpoints', type=str, nargs='+', default=DEFAULT_API_ENDPOINTS,
                        help='List of API endpoints to test (space-separated)')
    parser.add_argument('--payloads', type=str, nargs='+', default=DEFAULT_PAYLOADS,
                        help='List of payloads to use for testing (space-separated)')
    
    args = parser.parse_args()
    
    print("API Fuzzer - Running Security Testing...")
    api_fuzzer(args.base_url, args.endpoints, args.payloads)
    print("API Fuzzer - Completed. Check api_fuzzer.log for results.")
