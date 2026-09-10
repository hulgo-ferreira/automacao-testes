from guara.application import Application
from guara import it
from tests.fixtures.driver import driver
from tests.transactions.login_transaction import LoginWith

def test_login_com_credenciais_invalidas(driver):
    app = Application(driver)
    app.given(
        LoginWith,
        url="https://www.saucedemo.com",
        user="usuario_invalido",
        password="senha_invalida",
    ).then(it.Contains, "Username and password do not match")