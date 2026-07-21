from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage


class OrderPage(BasePage):
    """Страница заказа"""
    
    # ========== ЛОКАТОРЫ ==========
    # Первая страница
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_LIST = (By.XPATH, "//div[contains(@class, 'select-search__select')]//ul/li")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Вторая страница
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    RENTAL_PERIOD_OPTIONS = (By.XPATH, "//div[contains(@class, 'Dropdown-menu')]//div")
    BLACK_COLOR = (By.ID, "black")
    GREY_COLOR = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
    # Кнопка "Заказать" на второй странице формы
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button') and contains(@class, 'Button_Middle') and text()='Заказать']")
    
    # Модальное окно
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_Modal__')]//div[contains(text(), 'Заказ оформлен')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Order_Modal__')]//div[contains(text(), 'Заказ оформлен')]/following-sibling::div")

    # ========== МЕТОДЫ ==========

    def fill_first_page(self, name, surname, address, metro, phone):
        """Заполнение первой страницы формы"""
        # Закрываем куки-баннер если он есть
        self.close_cookie_banner()
        
        self.send_keys_to_element(self.NAME_FIELD, name)
        self.send_keys_to_element(self.SURNAME_FIELD, surname)
        self.send_keys_to_element(self.ADDRESS_FIELD, address)

        # Выбор станции метро
        self.click_element(self.METRO_FIELD)
        metro_elements = self.wait.until(EC.presence_of_all_elements_located(self.METRO_LIST))
        for metro_item in metro_elements:
            if metro in metro_item.text:
                metro_item.click()
                break

        self.send_keys_to_element(self.PHONE_FIELD, phone)
        self.click_element(self.NEXT_BUTTON)

    def fill_second_page(self, date, rental_period, color, comment):
        """Заполнение второй страницы формы"""
        self.send_keys_to_element(self.DATE_FIELD, date)
        self.click_body()  # Закрыть календарь

        # Выбор периода аренды
        self.click_element(self.RENTAL_PERIOD_DROPDOWN)
        period_elements = self.wait.until(EC.presence_of_all_elements_located(self.RENTAL_PERIOD_OPTIONS))
        for period in period_elements:
            if rental_period in period.text:
                period.click()
                break

        # Выбор цвета
        if color == "чёрный":
            self.click_element(self.BLACK_COLOR)
        elif color == "серый":
            self.click_element(self.GREY_COLOR)

        self.send_keys_to_element(self.COMMENT_FIELD, comment)
        
        # Кликаем на кнопку "Заказать" в форме
        self.click_element(self.ORDER_BUTTON)

    def confirm_order(self):
        """Подтверждение заказа в модальном окне"""
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_ORDER_BUTTON)).click()

    def is_order_success_displayed(self):
        """Проверка отображения сообщения об успешном заказе"""
        return self.is_element_displayed(self.SUCCESS_MESSAGE)

    def get_success_message_text(self):
        """Получение текста сообщения об успешном заказе"""
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_order_number(self):
        """Получение номера заказа"""
        return self.get_text(self.ORDER_NUMBER)