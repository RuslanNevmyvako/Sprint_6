from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    """Базовый класс с общими методами для всех страниц"""

    COOKIE_BUTTON = (By.XPATH, "//button[contains(@class, 'App_CookieButton')]")
    COOKIE_BANNER = (By.XPATH, "//div[contains(@class, 'App_CookieConsent__')]")
    BODY = (By.TAG_NAME, "body")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Клик по элементу: {locator}")
    def click_element(self, locator):
        """Клик по элементу с ожиданием кликабельности"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввод текста '{text}' в поле: {locator}")
    def send_keys_to_element(self, locator, text):
        """Ввод текста в поле"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста из элемента: {locator}")
    def get_text(self, locator):
        """Получение текста элемента"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Проверка видимости элемента: {locator}")
    def is_element_displayed(self, locator):
        """Проверка видимости элемента"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except TimeoutException:
            return False

    @allure.step("Проверка наличия элемента в DOM: {locator}")
    def is_element_present(self, locator):
        """Проверка наличия элемента в DOM (без ожидания видимости)"""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Скролл до элемента: {locator}")
    def scroll_to_element(self, locator):
        """Скролл до элемента"""
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Клик по элементу <body> (закрыть календарь/выпадающий список)")
    def click_body(self):
        """Клик по тегу body для закрытия календаря или выпадающего списка"""
        self.click_element(self.BODY)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        """Получение текущего URL"""
        return self.driver.current_url

    @allure.step("Ожидание, пока URL не будет содержать '{text}'")
    def wait_for_url_contains(self, text):
        """Ожидание, пока URL не будет содержать текст"""
        self.wait.until(lambda driver: text in driver.current_url)

    @allure.step("Закрытие куки-баннера")
    def close_cookie_banner(self):
        """
        Закрыть баннер с куки.
        Метод общий для всех страниц, так как баннер может появиться везде.
        """
        try:
            # Ждем кнопку с уменьшенным таймаутом (3 секунды)
            button = WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable(self.COOKIE_BUTTON)
            )
            button.click()
            print("✅ Куки-баннер закрыт")
            return True
        except:
            print("ℹ️ Куки-баннер не найден или уже закрыт")
            return False

    @allure.step("Получение идентификатора текущего окна")
    def get_current_window_handle(self):
        """Получить идентификатор текущего окна"""
        return self.driver.current_window_handle

    @allure.step("Переключение на окно: {window_handle}")
    def switch_to_window(self, window_handle):
        """Переключиться на указанное окно"""
        self.driver.switch_to.window(window_handle)

    @allure.step("Закрытие текущего окна")
    def close_current_window(self):
        """Закрыть текущее окно"""
        self.driver.close()

    @allure.step("Ожидание открытия нового окна и переключение на него")
    def switch_to_new_window(self, original_window):
        """Ожидать открытия нового окна и переключиться на него"""
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: len(d.window_handles) > 1
            )
        except TimeoutException:
            raise Exception("Новое окно не открылось")
        
        new_window = None
        for window in self.driver.window_handles:
            if window != original_window:
                new_window = window
                break
        
        if new_window is None:
            raise Exception("Новое окно не найдено")
        
        self.driver.switch_to.window(new_window)
        
        WebDriverWait(self.driver, 10).until(
            lambda d: d.current_url != "about:blank"
        )