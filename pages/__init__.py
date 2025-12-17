"""Классы Page Object для тестирования SauceDemo."""

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.constants import URLs, LoginPageLocators, InventoryPageLocators

__all__ = [
    "BasePage",
    "LoginPage",
    "InventoryPage",
    "URLs",
    "LoginPageLocators",
    "InventoryPageLocators",
]
