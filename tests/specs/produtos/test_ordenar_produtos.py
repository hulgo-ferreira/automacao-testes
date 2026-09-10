from selenium.webdriver.common.by import By
from guara import it
from guara.application import Application
from tests.fixtures.driver import driver
from tests.transactions.login_transaction import LoginWith

def test_ordenar_produtos_por_preco_crescente(driver):
    app = Application(driver)
    app.given(
        LoginWith,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce",
    ).then(it.Contains, "inventory")

    ordenacao = driver.find_element(By.CLASS_NAME, "product_sort_container")
    ordenacao.click()
    driver.find_element(By.CSS_SELECTOR, "option[value='lohi']").click()
    produtos = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    precos = [float(produto.text.replace("$", "")) for produto in produtos]

    assert precos == sorted(precos)