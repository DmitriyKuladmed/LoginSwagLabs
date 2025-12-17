"""Конфигурация pytest и фикстуры для тестов SauceDemo."""

import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="function")
def page(page: Page) -> Page:
    """Настроить страницу с параметрами по умолчанию.

    Args:
        page: Фикстура страницы Playwright из pytest-playwright.

    Yields:
        Настроенный экземпляр страницы.
    """
    # Установка таймаутов по умолчанию
    page.set_default_timeout(30000)
    page.set_default_navigation_timeout(30000)

    yield page


def pytest_configure(config: pytest.Config) -> None:
    """Настроить pytest с пользовательскими маркерами."""
    config.addinivalue_line(
        "markers", "smoke: отметить тест как smoke-тест"
    )
    config.addinivalue_line(
        "markers", "regression: отметить тест как регрессионный тест"
    )
