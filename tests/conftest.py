import random

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def email():
    first_names = ['anna', 'ivan', 'maria', 'pavel', 'elena',
                   'dmitry', 'olga', 'sergey', 'natalia', 'mikhail']
    last_names = ['ivanov', 'petrov', 'sidorov', 'smirnov',
                  'kuznetsov', 'popov', 'sokolov', 'novikov',
                  'morozov', 'volkov']

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    numbers = ''.join(str(random.randint(0, 9)) for _ in range(3))

    return f"{first_name}_{last_name}_{numbers}@yandex.ru"


@pytest.fixture
def log_in(driver):
    def _log_in():
        driver.find_element(By.CSS_SELECTOR, '[name="name"]').send_keys('kssenia_kononova_18_333@yandex.ru')
        driver.find_element(By.CSS_SELECTOR, '[name="Пароль"]').send_keys("723nvlh0")
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

    return _log_in
