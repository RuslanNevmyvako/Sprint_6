import pytest
from selenium import webdriver
from data import BASE_URL

@pytest.fixture
def driver():
    """Создает и закрывает браузер Firefox"""
    driver = webdriver.Firefox()  # Просто и понятно!
    driver.get(BASE_URL)
    yield driver
    driver.quit()