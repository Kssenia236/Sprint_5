# Тестирование Stellar Burgers
## Краткое описание
Проект автоматизации тестирования веб-приложения Stellar Burgers с использованием Python и Selenium WebDriver. Основная цель - проверка ключевого функционала пользовательского интерфейса.
## Реализованные тесты
### 1. Регистрация пользователей
- Проверка успешной регистрации с валидными данными(test_successful_registration_with_valid_credentials):
    - Корректное имя пользователя
    - Email в формате логин@домен
    - Пароль от 6 символов

- Проверка валидации некорректного пароля(test_registration_error_with_short_password)

### 2. Система авторизации
Тестирование входа через различные точки доступа:
- Кнопка "Войти в аккаунт" на главной странице(test_login_through_main_page_enter_account_button)
- Кнопка "Личный кабинет"(test_login_through_personal_account_button)
- Ссылка в форме регистрации(test_login_through_registration_form_link)
- Ссылка в форме восстановления пароля(test_login_through_forgot_password_form_link)

### 3. Переход в личный кабинет 
-переход по клику на «Личный кабинет»(test_personal_account_link_click_navigates_to_account_page)

### 4. Навигация по сайту
Тестирование переходов между разделами:
- Из личного кабинета в конструктор(test_constructor_link_click_navigates_to_constructor_page)
- Переход по логотипу(test_logo_click_navigates_to_main_page)

### 5. Тестирование выхода
- Проверка функции выхода из аккаунта(test_exit_from_account_in_profile)

### 6. Тестирование конструктора
Проверка навигации между секциями:
- Раздел "Булки"(test_navigate_to_buns_section)
- Раздел "Соусы"(test_navigate_to_sauces_section)
- Раздел "Начинки"(test_navigate_to_fillings_section)