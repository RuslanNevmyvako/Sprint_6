import pytest
from selenium import webdriver

BASE_URL = "https://qa-scooter.education-services.ru/"

@pytest.fixture
def driver():
    """Создает и закрывает браузер Firefox"""
    driver = webdriver.Firefox()  # Просто и понятно!
    driver.get(BASE_URL)
    yield driver
    driver.quit()