import allure
from page_objects.home_page import HomePage


class TestNavigation:
    """Тесты навигации по логотипам"""

    @allure.title("Переход на главную страницу по клику на логотип 'Самоката'")
    def test_scooter_logo_redirects_to_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.click_top_order_button()
        assert "/order" in home_page.get_current_url()
        home_page.click_scooter_logo()
        assert home_page.get_current_url() == "https://qa-scooter.education-services.ru/"

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
        assert "ya.ru" in driver.current_url, \
            f"Должен открыться Яндекс, текущий URL: {driver.current_url}"
        
        # Закрываем новое окно и возвращаемся
        home_page.close_current_window()
        home_page.switch_to_window(original_window)