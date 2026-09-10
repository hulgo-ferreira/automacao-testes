from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from guara.transaction import AbstractTransaction
from tests.pages.login_page import LoginPage

class LogoutWith(AbstractTransaction):

    def do(self, url, user, password):
        self._driver.get(url)
        page = LoginPage(self._driver)
        page.login(user, password)

        menu_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
        )
        menu_button.click()

        logout_link = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_link.click()

        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-button"))
        )

        return self._driver.current_url
