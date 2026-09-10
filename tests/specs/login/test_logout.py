from tests.fixtures.driver import driver
from guara.application import Application
from guara import it
from tests.transactions.logout_transaction import LogoutWith


def test_logout_com_sucesso(driver):
    app = Application(driver)
    app.given(
        LogoutWith,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce",
    ).then(it.Contains, "saucedemo.com")