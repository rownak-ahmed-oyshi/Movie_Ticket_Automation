import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# setup logging
logging.basicConfig(
    filename="Logs/TC_TB_005.log",
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
    number_of_tickets.send_keys("4")
    logging.info("Ticket Number Enter successfully.")

except Exception as e:
    logging.info("Element 'Number of Tickets' not found with Explicit wait.")

# 3. Select valid Ticket Class
try:
    ticket_class = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#price")))
    ticket_class_dropdown = Select(ticket_class)
    ticket_class_dropdown.select_by_value("2000")
    logging.info("Ticket Class VIP - $2000 selected.")

except Exception as e:
    logging.info("Element 'Ticket Class' not found with Explicit wait.")

# 4. Select valid registered user
try:
    registered_user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#user")))
    registered_user_dropdown = Select(registered_user)

    registered_user_dropdown.select_by_value("no")
    logging.info("Registered User - 'No' selected.")

except Exception as e:
    logging.info("Element 'Register User' not found with Explicit wait.")

# 5. Enter a valid Promo Code
try:
    promo_code = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#promo")))
    promo_code.send_keys("PROMO2027")
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

# Validate Ticket Price
expected_final_price = "Final Amount: 8000.00"
actual_final_price_element =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(6) > strong:nth-child(6)")))
actual_final_price = actual_final_price_element.text

if expected_final_price == actual_final_price:
    logging.info("Test Passed. Expected Final price match with Actual Final Price.")
else:
    logging.info("Test Failed. Expected Final Price does not match with Actual Final Price.")


logging.info("Script Complete.")
# driver.quit()
logging.info("End Browser Session...")