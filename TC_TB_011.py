import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# setup logging
logging.basicConfig(
    filename="Logs/TC_TB_011.log",
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
    promo_code.send_keys("<script>alert('XSS')</script>")
    logging.info("Injected malicious Promo Code for XSS test.")

except Exception as e:
    logging.info("Element 'Promo Code' not found with Explicit wait.")

# 6. Click on the "Book Now" button.
try:
    book_now_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='calculateBooking()']")))
    book_now_button.click()
    logging.info("Click on Book Now button successfully.")

except Exception as e:
    logging.info("Element 'Book now' button not found with Explicit wait.")


time.sleep(2)  # Let the DOM update, adjust if needed

page_source = driver.page_source

# Validate Error Message
expected_error_message = "Invalid input: Special characters or scripts are not allowed."

if expected_error_message in page_source:
    logging.info("Passed: XSS blocked and correct error message displayed.")
else:
    logging.error("Failed: XSS not blocked or error message not shown.")

logging.info("Script Complete.")
# driver.quit()
logging.info("End Browser Session...")