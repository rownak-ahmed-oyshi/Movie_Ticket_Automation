import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# setup logging
logging.basicConfig(
    filename="Logs/TC_TB_013.log",
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

# 3. Select valid Ticket Class
try:
    ticket_class = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#price")))
    ticket_class_dropdown = Select(ticket_class)
    ticket_class_dropdown.select_by_value("750")
    logging.info("Ticket Class Silver - $750 selected.")

except Exception as e:
    logging.info("Element 'Ticket Class' not found with Explicit wait.")

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

# Scrapping
# Validate Booking Successful
try:
    wait = WebDriverWait(driver, 20)

    # Step 1: Grab the success message
    success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "strong:nth-child(1)"))).text.strip()
    logging.info(f"Success Message: {success_message}")

    # Step 2: Grab the full result block text
    result_block = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#result"))).text.strip()

    # Step 3: Split the block into lines
    lines = result_block.split('\n')
    # lines should look like ['Tickets: 2', 'Total Price: 1500', 'Discount: 150.00', 'Final Amount: 1350.00']

    # Step 4: Parse each line into key-value
    result_data = {}
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            result_data[key.strip()] = value.strip()

    # Step 5: Define expected values
    expected_data = {
        "Tickets": "2",
        "Total Price": "$1500",
        "Discount": "$450.00",
        "Final Amount": "$1050.00"
    }

    # Step 6: Validate each field and log results
    for key, expected_value in expected_data.items():
        actual_value = result_data.get(key, None)
        if actual_value == expected_value:
            logging.info(f"{key}: {actual_value} - Test Passed.")
        else:
            logging.error(f"{key}: Expected '{expected_value}', Found '{actual_value}' - Test Failed.")

except Exception as e:
    logging.error(f"The symbol is not placed before the amount: {e}")


logging.info("Script Complete.")
# driver.quit()
logging.info("End Browser Session...")