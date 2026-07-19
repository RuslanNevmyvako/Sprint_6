import pytest
from page_objects.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class TestNavigation:
    """Тесты навигации по логотипам"""

    def test_scooter_logo_redirects_to_home_page(self, driver):
        """Переход на главную по клику на логотип 'Самоката'"""
        home_page = HomePage(driver)
        
        home_page.click_top_order_button()
        assert "/order" in home_page.get_current_url(), "Должны быть на странице заказа"
        
        home_page.click_scooter_logo()
        assert home_page.get_current_url() == "https://qa-scooter.education-services.ru/", \
            "Должен произойти переход на главную страницу"

    def test_yandex_logo_opens_ya_in_new_tab(self, driver):
        """Открытие Дзена в новой вкладке по клику на логотип Яндекса"""
        home_page = HomePage(driver)
        original_window = driver.current_window_handle
        windows_count = len(driver.window_handles)
        
        home_page.click_yandex_logo()
        
        try:
            WebDriverWait(driver, 10).until(
                lambda d: len(d.window_handles) > windows_count
            )
        except TimeoutException:
            pytest.fail("Новое окно не открылось")
        
        new_window = [w for w in driver.window_handles if w != original_window][0]
        driver.switch_to.window(new_window)
        
        WebDriverWait(driver, 10).until(
        lambda d: d.current_url != "about:blank")

        assert "ya.ru" in driver.current_url, \
            f"Должен открыться Яндекс, текущий URL: {driver.current_url}"
        
        driver.close()
        driver.switch_to.window(original_window)