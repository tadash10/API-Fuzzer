import requests

def test_session_management(api_endpoint, session_cookie):
    try:
        session = requests.Session()
        session.cookies['session'] = session_cookie

        response = session.get(api_endpoint, timeout=5)

        if 'Logged in' in response.text:
            return "Session management test passed (user logged in successfully)."
        else:
            return "Session management test failed (user not logged in)."
    except requests.exceptions.RequestException as e:
        return f"Session management test failed with an exception: {str(e)}"
