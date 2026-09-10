from guara.transaction import AbstractTransaction
from tests.pages.login_page import LoginPage
from selenium.webdriver.common.by import By


class LoginWith(AbstractTransaction):

    def do(self, url, user, password):
        self._driver.get(url)
        page = LoginPage(self._driver)
        page.login(user, password)

        if "inventory" in self._driver.current_url:
            return self._driver.current_url

        error_message = self._driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        return error_message.text