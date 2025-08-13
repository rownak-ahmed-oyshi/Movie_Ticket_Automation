from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BookingPage:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def enter_number_of_tickets(self, ticket_number):
        number_of_tickets = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tickets")))
        number_of_tickets.send_keys(str(ticket_number))

    def select_ticket_class(self, value):
        ticket_class = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#price")))
        ticket_class_dropdown = Select(ticket_class)
        ticket_class_dropdown.select_by_value(value)

    def select_registered_user(self,value):
        registered_user = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#user")))
        registered_user_dropdown = Select(registered_user)
        registered_user_dropdown.select_by_value(value)

    def enter_promo_code(self,promo_code):
        promo_code_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#promo")))
        promo_code_element.send_keys(promo_code)

    def click_book_button(self):
        book_now_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='calculateBooking()']")))
        book_now_button.click()

    def get_final_price(self):
        actual_final_price_element = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(6) > strong:nth-child(6)")))

        return actual_final_price_element.text

    def get_ticket_error_message(self):
        ticket_error_element = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#ticketError")))

        return ticket_error_element.text