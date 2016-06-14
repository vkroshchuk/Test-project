__author__ = 'kvi'

import pytest
from base_screen import BaseScreen


class LoginScreen(BaseScreen):
    def __init__(self, driver):
        super(LoginScreen, self).__init__(driver)

    email_locator = 'loginForm.username'
    password_locator = 'loginForm.password'
    login_button_locator = ''

    def login_with_credentials(self, email, password):
        self.driver.find_element_by_id(LoginScreen.email_locator).send_keys(email)
        self.driver.find_element_by_id(LoginScreen.password_locator).send_keys(password)
        self.driver.find_element_by_id(LoginScreen.login_button_locator).click()
