import logging
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from PIL import Image

# setup logging
logging.basicConfig(
    filename="../logs/TC_TB_006.log",
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

# Validate Dollar Sign
expected_final_price = "Final Amount: 1050.00$"
actual_final_price_element =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(6) > strong:nth-child(6)")))
actual_final_price = actual_final_price_element.text

if expected_final_price == actual_final_price:
    logging.info("Test Passed. Expected Dollar Sign Shown in the Display.")
else:
    logging.info("Test Failed. Expected Dollar Sign is not shown in the Display.")

    # get the page scroll dimensions
    width = driver.execute_script(f"return document.body.parentNode.scroll{"Width"}")
    height = driver.execute_script(f"return document.body.parentNode.scroll{"Height"}")

    # set the browser window size
    driver.set_window_size(width, height)

    # get the full body element
    full_body_element = driver.find_element(By.TAG_NAME, "body")

    # take a full-page screenshot
    full_body_element.screenshot("Bug_TC_TB_06.png")


logging.info("Script Complete.")
driver.quit()
logging.info("End Browser Session...")