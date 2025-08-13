import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

# setup logging
logging.basicConfig(
    filename="../Logs/TC_TB_010.log",
    level= logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Starting Browser Session...")

driver = webdriver.Firefox()
logging.info("Browser Launch Successfully.")

driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 20)

# 1. Navigate to the ticket booking page
driver.get("https://muntasir101.github.io/Movie-Ticket-Booking/")
logging.info("URL Open Successfully.")

# 2. Enter a valid Number of Tickets
try:
    number_of_tickets = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tickets")))
    number_of_tickets.send_keys("2")
    logging.info("Ticket Number Enter successfully.")

except Exception as e:
    logging.info("Element 'Number of Tickets' not found with Explicit wait.")



# 4. Select valid registered user
try:
    registered_user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#user")))
    registered_user_dropdown = Select(registered_user)

    registered_user_dropdown.select_by_value("yes")
    logging.info("Registered User - 'Yes' selected.")

except Exception as e:
    logging.info("Element 'Register User' not found with Explicit wait.")

# 5. Enter a valid Promo Code
try:
    promo_code = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#promo")))
    promo_code.send_keys("PROMO2025")
    logging.info("Valid Promo Code Enter successfully.")

except Exception as e:
    logging.info("Element 'Promo Code' not found with Explicit wait.")

# 6. Click on the "Book Now" button.
try:
    book_now_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='calculateBooking()']")))
    book_now_button.click()
    logging.info("Click on Book Now button successfully.")

except Exception as e:
    logging.info("Element 'Book now' button not found with Explicit wait.")

# Validate Error Message
expected_error_message = "Please select a Ticket Class."

try:
    # Check for the presence of the error message somewhere in the DOM
    error_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//*[contains(text(), 'Please select a Ticket Class')]"
        ))
    )
    actual_error_message = error_element.text.strip()

    if expected_error_message.lower() in actual_error_message.lower():
        logging.info("Passed: Correct error message displayed.")
    else:
        logging.info(f"Failed: Error message mismatch. Found: '{actual_error_message}'")

except TimeoutException:
    # Couldn’t find the error message, maybe because it defaulted to "Regular"
    logging.info("Failed: No error message shown. Booking continued with default Ticket Class.")


logging.info("Script Complete.")
# driver.quit()
logging.info("End Browser Session...")