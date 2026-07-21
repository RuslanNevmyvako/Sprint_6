import pytest
import allure
from page_objects.home_page import HomePage
from data import QUESTIONS_DATA


class TestQuestions:
    """Тесты раздела 'Вопросы о важном'"""

    @allure.title("Проверка раскрытия ответа на вопрос '{question_text}'")
    @pytest.mark.parametrize("question_index, question_text", QUESTIONS_DATA)
    def test_question_answer_displayed(self, driver, question_index, question_text):
        home_page = HomePage(driver)
        home_page.click_question(question_index)
        assert home_page.is_answer_displayed(question_index)
        assert len(home_page.get_answer_text(question_index)) > 0