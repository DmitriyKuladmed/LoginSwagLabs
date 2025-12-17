"""Базовый класс Page Object с общими методами."""

from playwright.sync_api import Page


class BasePage:
    """Базовый класс для всех page object."""

    def __init__(self, page: Page) -> None:
        """Инициализация базовой страницы с экземпляром Playwright page.

        Args:
            page: Экземпляр страницы Playwright.
        """
        self.page = page

    @property
    def current_url(self) -> str:
        """Получить текущий URL страницы.

        Returns:
            Строка с текущим URL.
        """
        return self.page.url

    def wait_for_url_contains(self, url_part: str, timeout: float = 30000) -> None:
        """Ожидать, пока URL не будет содержать указанную строку.

        Args:
            url_part: Часть URL для ожидания.
            timeout: Максимальное время ожидания в миллисекундах.
        """
        self.page.wait_for_url(f"**/{url_part}**", timeout=timeout)
