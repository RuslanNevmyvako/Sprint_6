import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ========== ЛОКАТОРЫ ==========
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_LIST = (By.XPATH, "//div[contains(@class, 'select-search__select')]//ul/li")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    RENTAL_PERIOD_OPTIONS = (By.XPATH, "//div[contains(@class, 'Dropdown-menu')]//div")
    BLACK_COLOR = (By.ID, "black")
    GREY_COLOR = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button') and contains(@class, 'Button_Middle') and text()='Заказать']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_Modal__')]//div[contains(text(), 'Заказ оформлен')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Order_Modal__')]//div[contains(text(), 'Заказ оформлен')]/following-sibling::div")

    # ========== МЕТОДЫ ==========
    def close_cookie_banner(self):
        """Закрыть баннер с куки"""
        try:
            cookie_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'App_CookieButton__')]")
            cookie_button.click()
            time.sleep(0.5)
            print("✅ Куки-баннер закрыт")
        except:
            print("ℹ️ Куки-баннер не найден или уже закрыт")

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys_to_element(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_element_displayed(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False

    def fill_first_page(self, name, surname, address, metro, phone):
        self.send_keys_to_element(self.NAME_FIELD, name)
        self.send_keys_to_element(self.SURNAME_FIELD, surname)
        self.send_keys_to_element(self.ADDRESS_FIELD, address)

        self.click_element(self.METRO_FIELD)
        metro_elements = self.wait.until(EC.presence_of_all_elements_located(self.METRO_LIST))
        for metro_item in metro_elements:
            if metro in metro_item.text:
                metro_item.click()
                break

        self.send_keys_to_element(self.PHONE_FIELD, phone)
        self.click_element(self.NEXT_BUTTON)

    def fill_second_page(self, date, rental_period, color, comment):
        self.send_keys_to_element(self.DATE_FIELD, date)
        self.driver.find_element(By.TAG_NAME, "body").click()

        self.click_element(self.RENTAL_PERIOD_DROPDOWN)
        period_elements = self.wait.until(EC.presence_of_all_elements_located(self.RENTAL_PERIOD_OPTIONS))
        for period in period_elements:
            if rental_period in period.text:
                period.click()
                break

        if color == "чёрный":
            self.click_element(self.BLACK_COLOR)
        elif color == "серый":
            self.click_element(self.GREY_COLOR)

        self.send_keys_to_element(self.COMMENT_FIELD, comment)
        self.click_element(self.ORDER_BUTTON)

    def confirm_order(self):
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_ORDER_BUTTON)).click()

    def is_order_success_displayed(self):
        return self.is_element_displayed(self.SUCCESS_MESSAGE)

    def get_success_message_text(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_order_number(self):
        return self.get_text(self.ORDER_NUMBER)