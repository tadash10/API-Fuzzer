
import re

def analyze_response(response_text):
    # Improved: Analyze the response for potential SQL errors more comprehensively
    sql_error_patterns = [
        r"SQL.*syntax.*error",
        r"database.*error",
        r"query.*failed",
    ]

    for pattern in sql_error_patterns:
        if re.search(pattern, response_text, re.IGNORECASE):
            return f"Potential SQL Injection detected in the response (Pattern: {pattern})."

    return "No known security vulnerabilities found in the response."
