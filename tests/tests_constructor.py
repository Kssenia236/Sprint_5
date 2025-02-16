from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import MainPageLocators


class TestConstructor():
    def test_navigate_to_fillings_section(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get('https://stellarburgers.nomoreparties.site')
        element = wait.until(
            EC.element_to_be_clickable((MainPageLocators.FILLINGS_BUTTON)))
        element.click()
        assert wait.until(EC.text_to_be_present_in_element(
            (MainPageLocators.BEEF_METEORITE_BUTTON),
            "Говяжий метеорит (отбивная)"
        ))

    def test_navigate_to_buns_section(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get('https://stellarburgers.nomoreparties.site')
        element = wait.until(
            EC.element_to_be_clickable((MainPageLocators.FILLINGS_BUTTON)))
        element.click()
        element = wait.until(
            EC.element_to_be_clickable((MainPageLocators.BUNS_BUTTON)))
        element.click()
        assert wait.until(EC.text_to_be_present_in_element(
            (MainPageLocators.FLUORESCENT_BUN_BUTTON),
            "Флюоресцентная булка R2-D3"
        ))

    def test_navigate_to_sauces_section(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get('https://stellarburgers.nomoreparties.site')
        element = wait.until(
            EC.element_to_be_clickable((MainPageLocators.SAUCES_BUTTON)))
        element.click()
        assert wait.until(EC.text_to_be_present_in_element(
            (MainPageLocators.SPICY_SAUCE_BUTTON),
            "Соус Spicy-X"
        ))
