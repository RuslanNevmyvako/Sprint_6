import allure
from page_objects.home_page import HomePage
from data import BASE_URL, ORDER_PATH

class TestNavigation:
    """Тесты навигации по логотипам"""

    @allure.title("Переход на главную страницу по клику на логотип 'Самоката'")
    def test_scooter_logo_redirects_to_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.click_top_order_button()
        
        # Проверяем, что URL содержит путь /order
        assert ORDER_PATH in home_page.get_current_url(), \
            f"Должны быть на странице заказа, текущий URL: {home_page.get_current_url()}"
        
        home_page.click_scooter_logo()
        
        # Проверяем, что URL равен BASE_URL
        assert home_page.get_current_url() == BASE_URL, \
            f"Должен произойти переход на главную страницу, текущий URL: {home_page.get_current_url()}"

    @allure.title("Открытие Яндекса в новой вкладке по клику на логотип 'Яндекса'")
    def test_yandex_logo_opens_ya_in_new_tab(self, driver):
        home_page = HomePage(driver)
        
        # Используем методы BasePage вместо прямого обращения к driver
        original_window = home_page.get_current_window_handle()
        
        home_page.click_yandex_logo()
        
        # Ожидаем открытия нового окна и переключаемся
        home_page.switch_to_new_window(original_window)
        
        # Проверяем URL
        current_url = home_page.get_current_url()
        assert "ya.ru" in current_url, \
            f"Должен открыться Яндекс или Дзен, текущий URL: {current_url}"
        
        # Закрываем новое окно и возвращаемся
        home_page.close_current_window()
        home_page.switch_to_window(original_window)