import pytest
from page_objects.home_page import HomePage


class TestQuestions:
    """Тесты раздела 'Вопросы о важном'"""
    
    QUESTIONS = [
        (0, "Сколько это стоит? И как оплатить?"),
        (1, "Хочу сразу несколько самокатов! Так можно?"),
        (2, "Как рассчитывается время аренды?"),
        (3, "Можно ли заказать самокат прямо на сегодня?"),
        (4, "Можно ли продлить заказ или вернуть самокат раньше?"),
        (5, "Вы привозите зарядку вместе с самокатом?"),
        (6, "Можно ли отменить заказ?"),
        (7, "Я жизу за МКАДом, привезёте?")
    ]

    @pytest.mark.parametrize("question_index, question_text", QUESTIONS)
    def test_question_answer_displayed(self, driver, question_index, question_text):
        """Проверка раскрытия ответа на каждый вопрос"""
        # Создаем объект страницы
        home_page = HomePage(driver)
        
        home_page.click_question(question_index)
        assert home_page.is_answer_displayed(question_index), \
            f"Ответ на вопрос '{question_text}' должен отображаться"
        
        answer_text = home_page.get_answer_text(question_index)
        assert len(answer_text) > 0, \
            f"Текст ответа на вопрос '{question_text}' не должен быть пустым"