from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainPageLocators


class TestRegistration:
    def test_registration_error_with_short_password(self, driver, email):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*MainPageLocators.NAME_INPUT).send_keys('Kssenia')
        driver.find_element(*MainPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*MainPageLocators.PASSWORD_INPUT).send_keys("72")
        driver.find_element(*MainPageLocators.REGISTER_BUTTON).click()
        assert driver.find_element(*MainPageLocators.PASSWORD_ERROR_MESSAGE).is_displayed()

    def test_successful_registration_with_valid_credentials(self, driver, email):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*MainPageLocators.NAME_INPUT).send_keys('Kssenia')
        driver.find_element(*MainPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*MainPageLocators.PASSWORD_INPUT).send_keys("723nvlh0")
        driver.find_element(*MainPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.REGISTER_BUTTON))
