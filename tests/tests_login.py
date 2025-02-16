from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import MainPageLocators


class TestLogIn():
    def test_login_through_main_page_enter_account_button(self, driver, log_in):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        log_in()
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.text_to_be_present_in_element(
            MainPageLocators.PLACE_ORDER_BUTTON,
            "Оформить заказ"
        ))

    def test_login_through_personal_account_button(self, driver, log_in):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        log_in()
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.text_to_be_present_in_element(
            MainPageLocators.PLACE_ORDER_BUTTON,
            "Оформить заказ"
        ))

    def test_login_through_forgot_password_form_link(self, driver, log_in):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        log_in()
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.text_to_be_present_in_element(
            MainPageLocators.PLACE_ORDER_BUTTON,
            "Оформить заказ"
        ))

    def test_login_through_registration_form_link(self, driver, log_in):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        log_in()
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.text_to_be_present_in_element(
            MainPageLocators.PLACE_ORDER_BUTTON,
            "Оформить заказ"
        ))
