
import os
from selenium.webdriver.common.by import By


def capture_full_page_screenshot(driver, screenshot_name):
    # Get the page scroll dimensions
    width = driver.execute_script("return document.body.parentNode.scrollWidth")
    height = driver.execute_script("return document.body.parentNode.scrollHeight")

    # Set the browser window size to the full page size
    driver.set_window_size(width, height)

    # Get the full body element
    full_body_element = driver.find_element(By.TAG_NAME, "body")

    # Ensure the Screenshots directory exists
    os.makedirs("Screenshots", exist_ok=True)

    # Create the full path for the screenshot file
    screenshot_path = os.path.join("Screenshots", f"{screenshot_name}.png")

    # Take a full-page screenshot
    full_body_element.screenshot(screenshot_path)
    # Screenshot

