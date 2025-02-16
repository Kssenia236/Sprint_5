from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainPageLocators


class TestPersonalAccount():

    def test_personal_account_link_click_navigates_to_account_page(self, driver, log_in):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        log_in()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
            MainPageLocators.PERSONAL_DATA_TEXT,
            "В этом разделе вы можете изменить свои персональные данные"
        ))
