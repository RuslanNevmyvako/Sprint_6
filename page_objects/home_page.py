from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ========== ЛОКАТОРЫ ==========
    TOP_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button') and contains(@class, 'Button_Middle') and text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    QUESTION_TEMPLATE = "//div[@id='accordion__heading-{}']"
    ANSWER_TEMPLATE = "//div[@id='accordion__panel-{}']"

    # ========== МЕТОДЫ ==========
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_element_displayed(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_current_url(self):
        return self.driver.current_url

    def click_top_order_button(self):
        self.click_element(self.TOP_ORDER_BUTTON)

    def click_bottom_order_button(self):
        self.wait.until(EC.presence_of_element_located(self.BOTTOM_ORDER_BUTTON))
        self.scroll_to_element(self.BOTTOM_ORDER_BUTTON)
        self.click_element(self.BOTTOM_ORDER_BUTTON)

    def click_question(self, question_index):
        locator = (By.XPATH, self.QUESTION_TEMPLATE.format(question_index))
        self.scroll_to_element(locator)
        self.click_element(locator)

    def is_answer_displayed(self, question_index):
        locator = (By.XPATH, self.ANSWER_TEMPLATE.format(question_index))
        return self.is_element_displayed(locator)

    def get_answer_text(self, question_index):
        locator = (By.XPATH, self.ANSWER_TEMPLATE.format(question_index))
        return self.get_text(locator)

    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)