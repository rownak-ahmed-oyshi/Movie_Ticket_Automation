import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# setup logging
logging.basicConfig(
    filename="Logs/TC_TB_007.log",
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


# 2. Click on the "Book Now" button.
try:
    book_now_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='calculateBooking()']")))
    book_now_button.click()
    logging.info("Click on Book Now button successfully.")

except Exception as e:
    logging.info("Element 'Book now' button not found with Explicit wait.")

# Validate Error Message
expected_error_message = "Please enter a number between 1 and 10."
actual_error_message_element =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ticketError")))
actual_error_message = actual_error_message_element.text

if expected_error_message == actual_error_message:
    logging.info("Test Passed. Expected Error Message Display Properly.")
else:
    logging.info("Test Failed. Expected Error Message Mismatched.")


logging.info("Script Complete.")
# driver.quit()
logging.info("End Browser Session...")