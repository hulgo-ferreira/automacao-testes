import time

import pytest
from tests.fixtures.driver import driver
from selenium.webdriver.common.by import By
from guara.application import Application
from guara import it
from tests.fixtures.driver import driver
from tests.transactions.login_transaction import LoginWith

@pytest.mark.smoke
def test_login_com_sucesso(driver):
    app = Application(driver)
    app.given(
        LoginWith,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce",
    ).then(it.Contains, "inventory")
 
def test_login_com_credenciais_invalidas(driver):
    app = Application(driver)
    app.given(
        LoginWith,
        url="https://www.saucedemo.com",
        user="usuario_invalido",
        password="senha_invalida",
    ).then(it.Contains, "Username and password do not match")
 
def test_login_usuario_bloqueado(driver):
    app = Application(driver)
    app.given(
        LoginWith,
        url="https://www.saucedemo.com",
        user="locked_out_user",
        password="secret_sauce",
    ).then(it.Contains, "Epic sadface: Sorry, this user has been locked out.")