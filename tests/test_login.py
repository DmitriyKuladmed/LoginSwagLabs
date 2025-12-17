"""Тесты логина для сайта SauceDemo."""

import allure
import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.epic("Аутентификация")
@allure.feature("Логин")
class TestLogin:
    """Тестовые сценарии для функциональности логина."""

    @allure.story("Успешный вход")
    @allure.title("Тест успешного входа с standard_user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self, page: Page) -> None:
        """Тест успешного входа с валидными учётными данными.

        Шаги:
            1. Открыть страницу логина
            2. Ввести валидное имя пользователя (standard_user)
            3. Ввести валидный пароль (secret_sauce)
            4. Нажать кнопку входа
            5. Проверить редирект на страницу инвентаря
        """
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert inventory_page.is_loaded(), "Страница инвентаря должна загрузиться"
        assert inventory_page.is_url_correct(), "URL должен содержать inventory.html"
        assert inventory_page.get_products_count() > 0, "Товары должны отображаться"

    @allure.story("Неудачный вход")
    @allure.title("Тест входа с неверным паролем")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_wrong_password(self, page: Page) -> None:
        """Тест входа с некорректным паролем.

        Шаги:
            1. Открыть страницу логина
            2. Ввести валидное имя пользователя
            3. Ввести неверный пароль
            4. Нажать кнопку входа
            5. Проверить отображение сообщения об ошибке
        """
        login_page = LoginPage(page)

        login_page.open()
        login_page.login("standard_user", "wrong_password")

        assert login_page.is_error_displayed(), "Должно отображаться сообщение об ошибке"
        error_text = login_page.get_error_message()
        assert "Username and password do not match" in error_text, (
            f"Ожидалась ошибка несоответствия пароля, получено: {error_text}"
        )

    @allure.story("Неудачный вход")
    @allure.title("Тест входа заблокированного пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_locked_out_user(self, page: Page) -> None:
        """Тест входа с заблокированной учётной записью.

        Шаги:
            1. Открыть страницу логина
            2. Ввести имя пользователя locked_out_user
            3. Ввести валидный пароль
            4. Нажать кнопку входа
            5. Проверить сообщение о блокировке
        """
        login_page = LoginPage(page)

        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")

        assert login_page.is_error_displayed(), "Должно отображаться сообщение об ошибке"
        error_text = login_page.get_error_message()
        assert "locked out" in error_text.lower(), (
            f"Ожидалась ошибка блокировки, получено: {error_text}"
        )

    @allure.story("Неудачный вход")
    @allure.title("Тест входа с пустыми полями")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_empty_fields(self, page: Page) -> None:
        """Тест входа с пустыми полями имени пользователя и пароля.

        Шаги:
            1. Открыть страницу логина
            2. Оставить поле имени пользователя пустым
            3. Оставить поле пароля пустым
            4. Нажать кнопку входа
            5. Проверить сообщение об обязательных полях
        """
        login_page = LoginPage(page)

        login_page.open()
        login_page.click_login()

        assert login_page.is_error_displayed(), "Должно отображаться сообщение об ошибке"
        error_text = login_page.get_error_message()
        assert "Username is required" in error_text, (
            f"Ожидалась ошибка обязательного поля, получено: {error_text}"
        )

    @allure.story("Успешный вход")
    @allure.title("Тест входа с performance_glitch_user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_performance_glitch_user(self, page: Page) -> None:
        """Тест входа с performance_glitch_user (возможны задержки).

        Шаги:
            1. Открыть страницу логина
            2. Ввести имя пользователя performance_glitch_user
            3. Ввести валидный пароль
            4. Нажать кнопку входа
            5. Ожидать редирект (с увеличенным таймаутом)
            6. Проверить успешный вход несмотря на возможные задержки
        """
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.open()
        login_page.login("performance_glitch_user", "secret_sauce")

        # Увеличенный таймаут для пользователя с задержками
        assert inventory_page.is_loaded(timeout=60000), (
            "Страница инвентаря должна загрузиться несмотря на задержки"
        )
        assert inventory_page.is_url_correct(), "URL должен содержать inventory.html"
        assert inventory_page.get_title() == "Products", (
            "Заголовок страницы должен быть 'Products'"
        )
