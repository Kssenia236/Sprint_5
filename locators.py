from selenium.webdriver.common.by import By


class MainPageLocators:
    NAME_INPUT = By.CSS_SELECTOR, '[name="name"]'  # локатор для поля ввода имени
    EMAIL_INPUT = By.CSS_SELECTOR, "form>fieldset:nth-child(2) input"  # поле ввода email
    PASSWORD_INPUT = By.CSS_SELECTOR, '[name="Пароль"]'  # поле ввода пароля
    REGISTER_BUTTON = By.CSS_SELECTOR, 'main button'  # кнопка зарегистрироваться и войти
    PASSWORD_ERROR_MESSAGE = By.CSS_SELECTOR, '.input__error'  # сообщение об ошибке ввода пароля
    PERSONAL_ACCOUNT_BUTTON = By.CSS_SELECTOR, '[href="/account"]'  # кнопка личный кабинет
    PERSONAL_DATA_TEXT = By.CSS_SELECTOR, 'main p'  # текст "В этом разделе вы можете изменить свои персональные данные"
    PLACE_ORDER_BUTTON = By.CSS_SELECTOR, 'main button'  # кнопка оформить заказ
    LOGOUT_BUTTON = By.XPATH, "//button[contains(@class, 'Account_button') and contains(text(), 'Выход')]"  # кнопка выхода
    FILLINGS_BUTTON = By.XPATH, '//div[contains(@class, "tab_tab")]//span[text()="Начинки"]/..'  # кнопка начинки
    BEEF_METEORITE_BUTTON = By.CSS_SELECTOR, '[alt="Говяжий метеорит (отбивная)"]'  # кнопка "Говяжий метеорит (отбивная)"
    BUNS_BUTTON = By.XPATH, '//div[contains(@class, "tab_tab")]//span[text()="Булки"]/..'  # кнопка булки
    FLUORESCENT_BUN_BUTTON = By.CSS_SELECTOR, '[alt="Флюоресцентная булка R2-D3"]'  # кнопка "Флюоресцентная булка R2-D3"
    SAUCES_BUTTON = By.XPATH, '//div[contains(@class, "tab_tab")]//span[text()="Соусы"]/..'  # кнопка соусы
    SPICY_SAUCE_BUTTON = By.CSS_SELECTOR, '[alt="Соус Spicy-X"]'  # кнопка "Соус Spicy-X"
    ASSEMBLE_BURGER_BUTTON = By.CSS_SELECTOR, 'main h1'  # заголовок "Соберите бургер"
    LOGO_BUTTON = By.CSS_SELECTOR, '[class="active"]'  # кнопка лого
