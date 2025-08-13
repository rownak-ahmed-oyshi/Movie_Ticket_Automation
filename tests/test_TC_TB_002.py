import logging

import pytest

from utils.screenshot_utils import capture_full_page_screenshot
from pages.booking_page import BookingPage
from utils.data_loader import load_booking_test_data

@pytest.mark.parametrize("test_case",load_booking_test_data("../data/booking_test_data_invalid.json")) #connecting data loader

def test_tc_tb_002(browser_config,test_case):
    logging.info("TC_TB_002 Started..")
    driver, wait = browser_config

    # Create object for booking page class
    booking_page = BookingPage(driver, wait)

    # 2. Enter a valid Number of Tickets
    try:
        booking_page.enter_number_of_tickets(test_case["tickets"])
        logging.info("Ticket Number Enter successfully.")

    except Exception as e:
        logging.info("Element 'Number of Tickets' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Ticket Number!!!")

    # 3. Select valid Ticket Class
    try:
        booking_page.select_ticket_class(test_case["class_value"])
        logging.info("Ticket Class Platinum - $1500 selected.")

    except Exception as e:
        logging.info("Element 'Ticket Class' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Ticket Class !!!")

    # 4. Select valid registered user
    try:
        booking_page.select_registered_user(test_case["user_value"])
        logging.info("Registered User - 'Yes' selected.")

    except Exception as e:
        logging.info("Element 'Register User' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Register User !!!")

    # 5. Enter a valid Promo Code
    try:
        booking_page.enter_promo_code(test_case["promo_code"])
        logging.info("Valid Promo Code Enter successfully.")

    except Exception as e:
        logging.info("Element 'Promo Code' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Promo Code !!!")

    # 6. Click on the "Book Now" button.
    try:
        booking_page.click_book_button()
        logging.info("Click on Book Now button successfully.")

    except Exception as e:
        logging.info("Element 'Book now' button not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Book Now Button !!!")

    # Validate Ticket Number Error Message
    expected_error_message = test_case["expected_error_message"]


    if expected_error_message == booking_page.get_ticket_error_message():
        logging.info("Test Passed. Error Message Display Properly.")

    else:
        logging.info("Test Failed. Error Message Mismatch.")

        # Screenshot
        capture_full_page_screenshot(driver, "BUG_TC_TB_02")

    logging.info("TC_TB_002 Completed..")
