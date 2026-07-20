from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import allure


class HomePage(BasePage):
    """Главная страница"""
    
    # ========== ЛОКАТОРЫ ==========
    TOP_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button') and contains(@class, 'Button_Middle') and text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    
    # Шаблоны для вопросов и ответов
    QUESTION_TEMPLATE = "//div[@id='accordion__heading-{}']"
    ANSWER_TEMPLATE = "//div[@id='accordion__panel-{}']"

    # ========== МЕТОДЫ ДЛЯ КНОПОК ==========
    
    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_top_order_button(self):
        """Клик по верхней кнопке 'Заказать'"""
        self.click_element(self.TOP_ORDER_BUTTON)

    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_bottom_order_button(self):
        """Клик по нижней кнопке 'Заказать'"""
        self.scroll_to_element(self.BOTTOM_ORDER_BUTTON)
        self.click_element(self.BOTTOM_ORDER_BUTTON)

    # ========== МЕТОДЫ ДЛЯ ВОПРОСОВ ==========
    
    @allure.step("Клик по вопросу #{question_index}")
    def click_question(self, question_index):
        """Клик по вопросу с указанным индексом"""
        locator = (By.XPATH, self.QUESTION_TEMPLATE.format(question_index))
        self.scroll_to_element(locator)
        self.click_element(locator)

    @allure.step("Проверка отображения ответа на вопрос #{question_index}")
    def is_answer_displayed(self, question_index):
        """Проверка отображения ответа на вопрос"""
        locator = (By.XPATH, self.ANSWER_TEMPLATE.format(question_index))
        return self.is_element_displayed(locator)

    @allure.step("Получение текста ответа на вопрос #{question_index}")
    def get_answer_text(self, question_index):
        """Получение текста ответа на вопрос"""
        locator = (By.XPATH, self.ANSWER_TEMPLATE.format(question_index))
        return self.get_text(locator)

    # ========== МЕТОДЫ ДЛЯ ЛОГОТИПОВ ==========
    
    @allure.step("Клик по логотипу 'Самокат'")
    def click_scooter_logo(self):
        """Клик по логотипу Самоката"""
        self.click_element(self.SCOOTER_LOGO)

    @allure.step("Клик по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        self.click_element(self.YANDEX_LOGO)