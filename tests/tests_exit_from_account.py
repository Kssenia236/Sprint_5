from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import MainPageLocators


class TestExit():

    def test_exit_from_account_in_profile(self, driver, log_in):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        log_in()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable(
            MainPageLocators.PERSONAL_ACCOUNT_BUTTON
        ))
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                MainPageLocators.LOGOUT_BUTTON)
        )
        element.click()
        assert wait.until(EC.text_to_be_present_in_element(
            MainPageLocators.REGISTER_BUTTON,
            "Войти"
        ))
