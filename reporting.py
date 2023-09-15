import json
from datetime import datetime

def generate_report(test_results):
    try:
        timestamp = get_current_timestamp()
        report = {
            "timestamp": timestamp,
            "results": test_results,
        }

        with open(f"api_fuzzer_report_{timestamp}.json", "w") as report_file:
            json.dump(report, report_file, indent=4)

        return f"Report generated: api_fuzzer_report_{timestamp}.json"
    except Exception as e:
        return f"Report generation failed with an exception: {str(e)}"

def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
