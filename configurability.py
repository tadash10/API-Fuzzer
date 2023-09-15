import argparse

def parse_command_line_args():
    try:
        parser = argparse.ArgumentParser(description="API Fuzzer - Security Testing Tool")
        parser.add_argument("--request-method", default="POST", help="HTTP request method (GET, POST, etc.)")
        parser.add_argument("--request-headers", nargs="*", help="Custom request headers")
        parser.add_argument("--timeout", type=int, default=10, help="Request timeout in seconds")
        parser.add_argument("--verbosity", type=int, default=1, help="Verbosity level (1 for basic, 2 for detailed)")
        return parser.parse_args()
    except argparse.ArgumentError as e:
        return f"Command line argument parsing failed with an error: {str(e)}"
