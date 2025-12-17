"""Page Object страницы логина SauceDemo."""

import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.constants import URLs, LoginPageLocators as Locators


class LoginPage(BasePage):
    """Page Object для страницы авторизации SauceDemo."""

    def __init__(self, page: Page) -> None:
        """Инициализация страницы логина.

        Args:
            page: Экземпляр страницы Playwright.
        """
        super().__init__(page)

    @allure.step("Открыть страницу логина")
    def open(self) -> "LoginPage":
        """Открыть страницу логина.

        Returns:
            Self для цепочки вызовов методов.
        """
        self.page.goto(URLs.BASE_URL)
        return self

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> "LoginPage":
        """Ввести имя пользователя в поле ввода.

        Args:
            username: Имя пользователя для ввода.

        Returns:
            Self для цепочки вызовов методов.
        """
        self.page.fill(Locators.USERNAME_INPUT, username)
        return self

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> "LoginPage":
        """Ввести пароль в поле ввода.

        Args:
            password: Пароль для ввода.

        Returns:
            Self для цепочки вызовов методов.
        """
        self.page.fill(Locators.PASSWORD_INPUT, password)
        return self

    @allure.step("Нажать кнопку входа")
    def click_login(self) -> None:
        """Нажать кнопку входа."""
        self.page.click(Locators.LOGIN_BUTTON)

    @allure.step("Выполнить вход с учётными данными: {username}")
    def login(self, username: str, password: str) -> None:
        """Выполнить вход с указанными учётными данными.

        Args:
            username: Имя пользователя.
            password: Пароль.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        """Получить текст сообщения об ошибке.

        Returns:
            Текст ошибки или пустая строка, если ошибки нет.
        """
        error_element = self.page.locator(Locators.ERROR_MESSAGE)
        if error_element.is_visible():
            return error_element.text_content() or ""
        return ""

    def is_error_displayed(self) -> bool:
        """Проверить, отображается ли сообщение об ошибке.

        Returns:
            True, если сообщение об ошибке видимо.
        """
        return self.page.locator(Locators.ERROR_MESSAGE).is_visible()
