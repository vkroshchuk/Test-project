#coding=utf-8
import allure                                                    #pytest
from core.base_test import BaseTest
from tele2.screens.base_screen import BaseScreen


class AboutAppTest(BaseTest):
    def setUp(self):
        self.base_screen = BaseScreen(self.driver)

    @allure.step                                        #may be allure.step?
    def test_1_login_webview_is_shown(self):
        # Test data
        expected_title = u'Översikt'

        # Test asserts
        self.assertEqual(self.driver.find_element_by_id("title").text, expected_title)
        self.driver.find_element_by_id("go_to_app_btn").click()
        self.base_screen.wait_loading()
        self.assertTrue(self.driver.find_element_by_xpath("//*[contains(@class, 'Button') and @content-desc='Logga in']").is_displayed())
        print'Pass. Login webview is shown'

    @allure.step
    def test_2_successful_login(self):
        #Test data

        login = 'hanna_lebanes@live.com'
        password = 'komplimang'

        # Test steps

        #need to add scroll
        #origin_el = self.driver.find_element_by_xpath("//*[contains(@class, 'Image') and @content-desc='tele2']")
        #destination_el = self.driver.find_element_by_xpath("//*[contains(@class, 'Button') and @content-desc='Logga in']")
        #self.driver.scroll(origin_el, destination_el)

        self.driver.find_element_by_xpath("//*[contains(@class, 'EditText') and @resource-id='loginForm.username']").send_keys(login)
        self.driver.find_element_by_xpath("//*[contains(@class, 'EditText') and @resource-id='loginForm.password']").send_keys(password)
        self.driver.find_element_by_xpath("//*[contains(@class, 'Button') and @content-desc='Logga in']").click()
        self.base_screen.wait_loading()
        self.assertTrue(self.driver.find_element_by_id('overview_statistic_btn').is_displayed())
        print'Pass. User is logged in. Overview is displayed'

    @allure.step
    def test_3_select_number_screen_is_opened(self):

        #Test steps:

        self.driver.find_element_by_xpath("//*[contains(@class, 'ImageButton') and @content-desc='MittTele2']").click()
        #self.assertTrue(self.driver.find_element_by_id('profile title').is_displayed())
        self.driver.find_element_by_id('menu_select_plan_secondary_title').click()
        self.base_screen.wait_loading()

        #find out how to determine swedish text in nav bar
        #self.assertTrue(self.driver.find_element_by_xpath("//*[contains(@class, 'TextView') and contains(text(), 'abonnemang')]"))
        self.assertTrue(self.driver.find_element_by_xpath("//*[contains(@class, 'TextView')]"))
        print "Pass. Choose subscription screen is opened"


    @allure.step
    def test_4_change_subscription_screen_is_opened(self):

        self.driver.find_element_by_xpath("//*[contains(@class, 'ImageButton') and @content-desc='MittTele2']").click()
        self.driver.find_element_by_id('menu_my_subscription_title').click()
        self.base_screen.wait_loading()
        self.assertTrue(self.driver.find_element_by_id("plan_caption"))
        print "Pass. Change subscription screen is opened"