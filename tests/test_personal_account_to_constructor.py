from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import MainPageLocators


class TestInputConstructor():

    def test_constructor_link_click_navigates_to_constructor_page(self, driver, log_in):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        log_in()
        wait = WebDriverWait(driver, 5)
        assert wait.until(EC.text_to_be_present_in_element(
            MainPageLocators.ASSEMBLE_BURGER_BUTTON,
            "Соберите бургер"
        ))

    def test_logo_click_navigates_to_main_page(self, driver, log_in):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        log_in()
        driver.find_element(*MainPageLocators.LOGO_BUTTON).click()
        wait = WebDriverWait(driver, 5)
        assert wait.until(EC.text_to_be_present_in_element(
            MainPageLocators.ASSEMBLE_BURGER_BUTTON,
            "Соберите бургер"
        ))
