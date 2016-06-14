#__author__ = 'kvi'

import pytest
from time import sleep


class BaseScreen(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_loading(self):
        loader_displayed = True
        while loader_displayed:
            try:
                loader_displayed = self.driver.find_element_by_id('auth_progress_bar').is_displayed()
                sleep(1)
            except:
                loader_displayed = False
                sleep(1)
                # End of the while

