import pytest
import allure
from page_objects.home_page import HomePage
from page_objects.order_page import OrderPage
from data import ORDERS_DATA


class TestOrder:
    """Тесты оформления заказа"""

    @allure.title("Позитивный сценарий заказа через верхнюю кнопку: {order[name]}")
    @pytest.mark.parametrize("order", [o for o in ORDERS_DATA if o["button"] == "top"])
    def test_positive_order_top_button(self, driver, order):
        """Заказ через верхнюю кнопку"""
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        
        home_page.close_cookie_banner()
        home_page.click_top_order_button()

        order_page.fill_first_page(
            name=order["name"],
            surname=order["surname"],
            address=order["address"],
            metro=order["metro"],
            phone=order["phone"]
        )

        order_page.fill_second_page(
            date=order["date"],
            rental_period=order["rental_period"],
            color=order["color"],
            comment=order["comment"]
        )

        order_page.confirm_order()

        assert order_page.is_order_success_displayed()
        assert "Заказ оформлен" in order_page.get_success_message_text()
        assert order_page.get_order_number()

    @allure.title("Позитивный сценарий заказа через нижнюю кнопку: {order[name]}")
    @pytest.mark.parametrize("order", [o for o in ORDERS_DATA if o["button"] == "bottom"])
    def test_positive_order_bottom_button(self, driver, order):
        """Заказ через нижнюю кнопку"""
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        
        home_page.close_cookie_banner()
        home_page.click_bottom_order_button()

        order_page.fill_first_page(
            name=order["name"],
            surname=order["surname"],
            address=order["address"],
            metro=order["metro"],
            phone=order["phone"]
        )

        order_page.fill_second_page(
            date=order["date"],
            rental_period=order["rental_period"],
            color=order["color"],
            comment=order["comment"]
        )

        order_page.confirm_order()

        assert order_page.is_order_success_displayed()
        assert "Заказ оформлен" in order_page.get_success_message_text()
        assert order_page.get_order_number()