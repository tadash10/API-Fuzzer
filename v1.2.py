import requests

# List of common API endpoints to fuzz
api_endpoints = [
    "/api/v1/login",
    "/api/v1/user",
    "/api/v1/products",
    "/api/v1/orders",
    # Add more endpoints as needed
]

# List of common payloads for security testing
payloads = [
    "<script>alert('XSS')</script>",
    "1' OR '1'='1",
    "SELECT * FROM users;",
    # Add more payloads for SQL injection, XSS, and other tests
]

# Base URL of the target API
base_url = "https://api.example.com"

# Function to fuzz test API endpoints
def api_fuzzer():
    try:
        for endpoint in api_endpoints:
            for payload in payloads:
                url = base_url + endpoint
                headers = {"Content-Type": "application/json"}
                data = {"param": payload}

                response = requests.post(url, json=data, headers=headers)

                # Check for potential vulnerabilities in the response
                if "error" in response.text.lower():
                    print(f"Potential vulnerability found at {url} with payload: {payload}")
                elif response.status_code == 200:
                    print(f"Successful response at {url} with payload: {payload}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nScript terminated by user.")

if __name__ == "__main__":
    print("API Fuzzer - Educational Use Only")
    print("=================================")
    api_fuzzer()
