import pytest
from page_objects.home_page import HomePage
from page_objects.order_page import OrderPage


class TestOrder:
    """Тесты оформления заказа"""
    
    ORDERS = [
        {
            "name": "Иван",
            "surname": "Петров",
            "address": "ул. Ленина 1",
            "metro": "Сокольники",
            "phone": "+79111111111",
            "date": "20.07.2026",
            "rental_period": "сутки",
            "color": "чёрный",
            "comment": "Позвоните за 10 минут",
            "button": "top"
        },
        {
            "name": "Мария",
            "surname": "Смирнова",
            "address": "пр. Вернадского 15",
            "metro": "Парк культуры",
            "phone": "+79222222222",
            "date": "22.07.2026",
            "rental_period": "пятеро суток",
            "color": "серый",
            "comment": "Оставьте у консьержа",
            "button": "bottom"
        }
    ]

    @pytest.mark.parametrize("order", ORDERS, ids=[
        f"{order['name']} - {order['button']}" 
        for order in ORDERS
    ])
    def test_positive_order_flow(self, driver, order):
        """Позитивный сценарий заказа с разными данными"""
        # Создаем объекты страниц прямо в тесте
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        
        if order["button"] == "top":
            home_page.click_top_order_button()
        else:
            home_page.click_bottom_order_button()
        
        order_page.close_cookie_banner()

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

        assert order_page.is_order_success_displayed(), \
            "Должно появиться сообщение об успешном создании заказа"
        
        success_message = order_page.get_success_message_text()
        assert "Заказ оформлен" in success_message, \
            f"Сообщение должно содержать 'Заказ оформлен', получено: {success_message}"
        
        order_number = order_page.get_order_number()
        assert order_number and len(order_number) > 0, \
            "Номер заказа должен отображаться"