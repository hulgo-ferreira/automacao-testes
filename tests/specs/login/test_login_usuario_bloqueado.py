from guara.application import Application
from guara import it
from tests.fixtures.driver import driver
from tests.transactions.login_transaction import LoginWith

def test_login_usuario_bloqueado(driver):
    app = Application(driver)
    app.given(
        LoginWith,
        url="https://www.saucedemo.com",
        user="locked_out_user",
        password="secret_sauce",
    ).then(it.Contains, "Epic sadface: Sorry, this user has been locked out.")