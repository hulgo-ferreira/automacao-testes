import time
 
from tests.fixtures.driver import driver
from selenium.webdriver.common.by import By

def test_continuar_comprando_apos_adicionar_item(driver):
 
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert "cart.html" in driver.current_url
 
    driver.find_element(By.ID, "continue-shopping").click()
    assert "inventory.html" in driver.current_url
 
    produtos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(produtos) > 0