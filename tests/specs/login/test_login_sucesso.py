from tests.fixtures.driver import driver
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from guara.application import Application
from selenium import webdriver
from guara import it
from tests.transactions.login_transaction import LoginWith
from tests.fixtures.driver import driver

def test_login_com_sucesso(driver):
    app = Application(driver)
    app.given(
        LoginWith,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce",
    ).then(it.Contains, "inventory")

