"""Page Object страницы инвентаря SauceDemo."""

from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.constants import URLs, InventoryPageLocators as Locators


class InventoryPage(BasePage):
    """Page Object для страницы инвентаря SauceDemo."""

    def __init__(self, page: Page) -> None:
        """Инициализация страницы инвентаря.

        Args:
            page: Экземпляр страницы Playwright.
        """
        super().__init__(page)

    def is_loaded(self, timeout: float = 30000) -> bool:
        """Проверить, загружена ли страница инвентаря.

        Args:
            timeout: Максимальное время ожидания в миллисекундах.

        Returns:
            True, если страница успешно загружена.
        """
        try:
            self.page.wait_for_selector(
                Locators.INVENTORY_CONTAINER, state="visible", timeout=timeout
            )
            return True
        except Exception:
            return False

    def get_title(self) -> str:
        """Получить текст заголовка страницы.

        Returns:
            Текст заголовка.
        """
        return self.page.locator(Locators.TITLE).text_content() or ""

    def is_url_correct(self) -> bool:
        """Проверить, содержит ли текущий URL путь инвентаря.

        Returns:
            True, если URL корректный.
        """
        return URLs.INVENTORY_PATH in self.current_url

    def get_products_count(self) -> int:
        """Получить количество отображаемых товаров.

        Returns:
            Количество товаров.
        """
        return self.page.locator(Locators.PRODUCT_ITEM).count()
