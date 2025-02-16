from selenium.webdriver.common.by import By


class MainPageLocators():
    NAME_INPUT = (By.CSS_SELECTOR, '[name="name"]')  # локатор для поля ввода имени
    EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')  # поле ввода email
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="Пароль"]')  # поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')  # кнопка зарегистрироваться и войти
    PASSWORD_ERROR_MESSAGE = (By.CSS_SELECTOR, '.input__error')  # сообщение об ошибке ввода пароля
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p')  # кнопка личный кабинет
    PERSONAL_DATA_TEXT = (By.XPATH,
                          '//*[@id="root"]/div/main/div/nav/p')  # текст "В этом разделе вы можете изменить свои персональные данные"
    PLACE_ORDER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')  # кнопка оформить заказ
    LOGOUT_BUTTON = (
    By.XPATH, "//button[contains(@class, 'Account_button') and contains(text(), 'Выход')]")  # кнопка выхода
    FILLINGS_BUTTON = (By.XPATH, '//div[contains(@class, "tab_tab")]//span[text()="Начинки"]/..')  # кнопка начинки
    BEEF_METEORITE_BUTTON = (
    By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[2]/p')  # кнопка "Говяжий метеорит (отбивная)"
    BUNS_BUTTON = (By.XPATH, '//div[contains(@class, "tab_tab")]//span[text()="Булки"]/..')  # кнопка булки
    FLUORESCENT_BUN_BUTTON = (
    By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/p')  # кнопка "Флюоресцентная булка R2-D3"
    SAUCES_BUTTON = (By.XPATH, '//div[contains(@class, "tab_tab")]//span[text()="Соусы"]/..')  # кнопка соусы
    SPICY_SAUCE_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[1]/p')  # кнопка "Соус Spicy-X"
    ASSEMBLE_BURGER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')  # кнопка "Соберите бургер"
    LOGO_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/div/a") # кнопка лого
