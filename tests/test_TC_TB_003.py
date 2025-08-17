import logging
import pytest
import os
import datetime

from utils.bug_report_template import generate_bug_report, save_bug_report
from utils.screenshot_utils import capture_full_page_screenshot
from pages.booking_page import BookingPage
from utils.data_loader import load_booking_test_data

# Use the 'invalid_bookings' key to load the data
invalid_data = load_booking_test_data("invalid_bookings")

# Select only the first element (index 0) and wrap it in a list
first_invalid_case = [invalid_data[0]]


@pytest.mark.parametrize("test_case", first_invalid_case)
def test_tc_tb(browser_config, test_case):
    test_case_name = "TC_TB_003"
    logging.info(f"{test_case_name} Started..")
    driver, wait = browser_config
    booking_page = BookingPage(driver, wait)

    # 2. Enter a valid Number of Tickets
    try:
        booking_page.enter_number_of_tickets(test_case["tickets"])
        logging.info("Ticket Number Enter successfully.")
    except Exception as e:
        logging.error("Element 'Number of Tickets' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Ticket Number !!!")

    # 3. Select valid Ticket Class
    try:
        booking_page.select_ticket_class(test_case["class_value"])
        logging.info("Ticket Class Silver - $750 selected.")
    except Exception as e:
        logging.error("Element 'Ticket Class' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Ticket Class !!!")

    # 4. Select valid registered user
    try:
        booking_page.select_registered_user(test_case["user_value"])
        logging.info("Registered User - 'Yes' selected.")
    except Exception as e:
        logging.error("Element 'Register User' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Register User !!!")

    # 5. Enter a valid Promo Code
    try:
        booking_page.enter_promo_code(test_case["promo_code"])
        logging.info("Valid Promo Code Enter successfully.")
    except Exception as e:
        logging.error("Element 'Promo Code' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Promo Code !!!")

    # 6. Click on the "Book Now" button.
    try:
        booking_page.click_book_button()
        logging.info("Click on Book Now button successfully.")
    except Exception as e:
        logging.error("Element 'Book now' button not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Book Now Button !!!")

    # Validate the error message
    expected_error_message = test_case.get("error_message")
    actual_error_message = booking_page.get_ticket_error_message()

    if expected_error_message == actual_error_message:
        logging.info("Test Passed. Expected Error Message matches Actual Error Message.")
    else:
        logging.info("Test Failed. Expected Error Message does not match with Actual Error Message!.")

        # Take a screenshot on failure and save the path
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_filename = f"{test_case_name}_failure_{timestamp}.png"
        screenshot_path = os.path.join("logs", "bug_reports", screenshot_filename)
        capture_full_page_screenshot(driver, screenshot_path)

        # Generate the bug report string using the new function
        bug_report_content = generate_bug_report(test_case, actual_error_message, expected_error_message,
                                                 screenshot_path, test_case_name)

        # Save the report to a separate file using the new function
        save_bug_report(bug_report_content, test_case_name)

        pytest.fail("Test failed due to incorrect error message.")

    logging.info(f"{test_case_name} Completed..")