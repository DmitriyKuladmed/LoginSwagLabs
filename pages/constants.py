"""Константы и локаторы для страниц SauceDemo."""


class URLs:
    """Константы URL."""

    BASE_URL = "https://www.saucedemo.com/"
    INVENTORY_PATH = "inventory.html"


class LoginPageLocators:
    """Локаторы для страницы логина."""

    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"


class InventoryPageLocators:
    """Локаторы для страницы инвентаря."""

    INVENTORY_CONTAINER = ".inventory_container"
    TITLE = ".title"
    PRODUCT_ITEM = ".inventory_item"
