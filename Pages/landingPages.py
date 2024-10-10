import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from Utilities.scroll_util import ScrollUtil


class landingpages:
    # username = configReader.readConfig('prod_credentials', 'username')
    # password = configReader.readConfig('prod_credentials', 'password')

    def __init__(self,driver):
        self.driver = driver

    get_started = (AppiumBy.ID, "com.embibe.student:id/tvLogin")
    stu_email_field = (AppiumBy.ID, "com.embibe.student:id/etEmailID")
    click_using_password_link = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.embibe.student:id/tvSignInWithOtp']")
    stu_password_field = (AppiumBy.ID, "com.embibe.student:id/etPassword")
    stu_proceed_btn = (AppiumBy.ID, "com.embibe.student:id/tvSignIn")
    stu_OTP_btn_click = (AppiumBy.XPATH, "//*[@text='Get OTP']")
    tos = (AppiumBy.XPATH, "//*[@text='Terms and Conditions']")
    privacypolicy = (AppiumBy.XPATH, "//*[@text='Privacy Policy']")
    forgot_password_link = (AppiumBy.ID, "com.embibe.student:id/tvForgotPassword")
    forgot_email_field = (AppiumBy.ID, "com.embibe.student:id/et_emailMobile")
    location_continue_btn = (AppiumBy.ID, 'com.embibe.student:id/btn_continue_location_access')
    loc_not_allow = (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')


    def signinusingpassword(self):
        self.driver.find_element(*landingpages.location_continue_btn).click()
        self.driver.find_element(*landingpages.loc_not_allow).click()
        self.driver.find_element(*landingpages.get_started).click()
        self.driver.find_element(*landingpages.stu_email_field).click()
        self.driver.find_element(*landingpages.click_using_password_link).click()
        self.driver.find_element(*landingpages.stu_email_field).send_keys('9035371071')
        self.driver.find_element(*landingpages.stu_password_field).send_keys('Embibe@1')
        time.sleep(3)
        self.driver.find_element(*landingpages.stu_proceed_btn).click()
        time.sleep(10)

    def tosinsigninpage(self):
        self.driver.find_element(*landingpages.location_continue_btn).click()
        self.driver.find_element(*landingpages.loc_not_allow).click()
        self.driver.find_element(*landingpages.get_started).click()
        self.driver.find_element(*landingpages.tos).click()
        time.sleep(5)
        ScrollUtil.swipeUp(3, self.driver)
        ScrollUtil.swipeDown(2, self.driver)
        self.driver.press_keycode(4)


    def privacypolicyinsigninpage(self):
        self.driver.find_element(*landingpages.location_continue_btn).click()
        self.driver.find_element(*landingpages.loc_not_allow).click()
        self.driver.find_element(*landingpages.get_started).click()
        self.driver.find_element(*landingpages.privacypolicy).click()
        time.sleep(5)
        ScrollUtil.swipeUp(3, self.driver)
        ScrollUtil.swipeDown(2, self.driver)
        self.driver.press_keycode(4)


    def signinusingOTP(self):
        self.driver.find_element(*landingpages.location_continue_btn).click()
        self.driver.find_element(*landingpages.loc_not_allow).click()
        self.driver.find_element(*landingpages.get_started).click()
        self.driver.find_element(*landingpages.stu_email_field).click()
        self.driver.find_element(*landingpages.stu_email_field).send_keys('9035371071')
        self.driver.find_element(*landingpages.stu_OTP_btn_click).click()
        time.sleep(10)

    def clickTOS(self):
        self.driver.find_element(*landingpages.location_continue_btn).click()
        self.driver.find_element(*landingpages.loc_not_allow).click()
        self.driver.find_element(*landingpages.tos).click()
        time.sleep(5)
        ScrollUtil.swipeUp(3, self.driver)
        ScrollUtil.swipeDown(2, self.driver)
        self.driver.press_keycode(4)
        # try:
        #     if self.driver.find_element(*landingpages.location_continue_btn).is_displayed():
        #         self.driver.find_element(*landingpages.location_continue_btn).click()
        #         self.driver.find_element(*landingpages.loc_not_allow).click()
        #         self.driver.find_element(*landingpages.get_started).click()
        #         self.driver.find_element(*landingpages.privacypolicy).click()
        # except NoSuchElementException:
        #     self.driver.find_element(*landingpages.loc_not_allow).click()
        #     self.driver.find_element(*landingpages.get_started).click()
        #     self.driver.find_element(*landingpages.tos).click()

    def clickPrivacyPolicy(self):
        self.driver.find_element(*landingpages.location_continue_btn).click()
        self.driver.find_element(*landingpages.loc_not_allow).click()
        self.driver.find_element(*landingpages.privacypolicy).click()
        time.sleep(5)
        ScrollUtil.swipeUp(3, self.driver)
        ScrollUtil.swipeDown(2, self.driver)
        self.driver.press_keycode(4)
        # try:
        #     if self.driver.find_element(*landingpages.location_continue_btn).is_displayed():
        #         self.driver.find_element(*landingpages.location_continue_btn).click()
        #         self.driver.find_element(*landingpages.loc_not_allow).click()
        #         self.driver.find_element(*landingpages.get_started).click()
        #         self.driver.find_element(*landingpages.privacypolicy).click()
        # except NoSuchElementException:
        #     self.driver.find_element(*landingpages.loc_not_allow).click()
        #     self.driver.find_element(*landingpages.get_started).click()
        #     self.driver.find_element(*landingpages.privacypolicy).click()


    def clickforgotpassword(self):
        self.driver.find_element(*landingpages.location_continue_btn).click()
        self.driver.find_element(*landingpages.loc_not_allow).click()
        self.driver.find_element(*landingpages.get_started).click()
        self.driver.find_element(*landingpages.click_using_password_link).click()
        self.driver.find_element(*landingpages.forgot_password_link).click()
        self.driver.find_element(*landingpages.forgot_email_field).click()
        self.driver.find_element(*landingpages.forgot_email_field).send_keys("9035371071")
        self.driver.find_element(*landingpages.stu_OTP_btn_click).click()
        time.sleep(10)









