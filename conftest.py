import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.wait import WebDriverWait

# setup logging
logging.basicConfig(
    filename="logs/TC_All_Logs.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def pytest_addoption(parser):
    """Adds a command-line option to select the browser."""
    parser.addoption("--browser", action="store", default="firefox",
                     help="Browser to run tests on: chrome, firefox, or edge")


@pytest.fixture(scope="function")
def browser_config(request):
    """
    Configures and returns a Selenium WebDriver instance based on the
    --browser command-line option.
    """
    browser_type = request.config.getoption("--browser").lower()
    driver = None
    logging.info(f"Starting browser session with {browser_type}...")

    if browser_type == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headed")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_type == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headed")
        driver = webdriver.Firefox(options=firefox_options)
    elif browser_type == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--headed")
        driver = webdriver.Edge(options=edge_options)
    else:
        raise ValueError(f"Unsupported browser type: {browser_type}")

    logging.info(f"{browser_type} browser launched successfully.")

    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 20)
    driver.get("https://muntasir101.github.io/Movie-Ticket-Booking/")
    logging.info("URL opened successfully.")

    yield driver, wait

    logging.info("Script complete.")
    driver.quit()
    logging.info("Ending browser session...")
    logging.info("...................")
    logging.info("...................")