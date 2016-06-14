import os
import unittest
from appium import webdriver
import allure                                     #pytest
from time import sleep

PLATFORM_NAME = 'Android'
PLATFORM_VERSION = '5.1'
DEVICE_NAME = 'xt1097-TA9890BG2I'
PROJECT_PATH = 'C:/Users/kvi.KYIV/PycharmProjects/appy-master'
APP_PATH = 'C:/Users/kvi.KYIV/Desktop/MittTele2_Android-prod-release-1098.apk'
APP_PACKAGE = 'swe.tele2.mittTele2'
APP_ACTIVITY = 'swe.tele2.mittTele2/swe.tele2.mitttele2.ui.startup.SplashScreenActivity'
HOST = 'http://127.0.0.1:4723/wd/hub'


class BaseTest(unittest.TestCase):

    @classmethod                               #may be it should be deleted
    def set_driver(cls):
        desired_caps = {'platformName': PLATFORM_NAME,
                        'platformVersion': PLATFORM_VERSION,
                        'deviceName': DEVICE_NAME,
                        'app': os.path.join(PROJECT_PATH, APP_PATH),
                        'appPackage': APP_PACKAGE,
                        #'appActivity': APP_ACTIVITY,
                        }

        # Returns abs path relative to this file and not cwd
        cls.driver = webdriver.Remote(HOST, desired_caps)

    # @allure.step('Set up') it should be added instead of @classmethod ???
    @classmethod
    def setUpClass(cls):
        cls.set_driver()

    #@allure.step('Tear down') it should be added instead of @classmethod ???
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def test_initial_test(self):
    #     print self.driver._is_remote