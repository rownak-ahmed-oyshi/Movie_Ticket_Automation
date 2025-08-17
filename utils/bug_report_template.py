import os
import datetime
import logging


def generate_bug_report(test_case, actual_message, expected_message, screenshot_path, test_case_name="TC_TB_003"):
    """
    Generates a formatted bug report string with details from the test case.
    """
    report = f"""
================ BUG REPORT ================
Test Case: {test_case_name}
Description: An invalid booking scenario failed as the expected error message did not match the actual message.
--------------------------------------------
Test Data:
  Tickets: {test_case.get("tickets")}
  Class Value: {test_case.get("class_value")}
  User Value: {test_case.get("user_value")}
  Promo Code: {test_case.get("promo_code")}
--------------------------------------------
Validation Failure:
  Expected Message: {expected_message}
  Actual Message:   {actual_message}
--------------------------------------------
Screenshot: {os.path.abspath(screenshot_path)}
============================================
"""
    return report


def save_bug_report(report_content, test_case_name):
    """
    Writes a bug report to a new file inside the logs/bug_reports directory.
    """
    # Create a timestamp to ensure a unique filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create the bug_reports directory if it doesn't exist
    report_dir = os.path.join("bug_reports")
    os.makedirs(report_dir, exist_ok=True)

    # Create a unique filename for the bug report
    report_filename = f"bug_report_{test_case_name}_{timestamp}.txt"
    file_path = os.path.join(report_dir, report_filename)

    with open(file_path, "w") as f:
        f.write(report_content)
    logging.info(f"Bug report saved to: {file_path}")
    return file_path