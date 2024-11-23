import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Pages.searchpage import Search_Module
from Utilities.scroll_util import ScrollUtil


class TestHome:

    def __init__(self, driver):
        self.driver = driver


    custom_test_tile = AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.embibe.student:id/create_own_test"]'
    continue_btn = AppiumBy.ID, 'com.embibe.student:id/btn_continue'
    test_tab = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/navigation_bar_item_icon_container"])[4]'
    guided_tour_cancel_btn = AppiumBy.ID, 'com.embibe.student:id/ivClose'
    quick_5_min_test_btn = AppiumBy.ID, 'com.embibe.student:id/btn_quick_five_min_test'
    custom_test_btn = AppiumBy.ID, 'com.embibe.student:id/btn_continue'
    test_name_field = AppiumBy.ID, 'com.embibe.student:id/et_test_name'
    create_test_btn = AppiumBy.ID, 'com.embibe.student:id/btn_create_test'
    test_btn = AppiumBy.ID, 'com.embibe.student:id/btnTakeTest'
    sel_new_embibe_expUI = AppiumBy.ID, 'com.embibe.student:id/btn_continue'
    test_env_popup= AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_parent_close_video"]/android.view.ViewGroup'
    instruc_next_button = AppiumBy.ID, 'com.embibe.student:id/btn_next'
    instruct_chkbox = AppiumBy.ID, 'com.embibe.student:id/iv_checkbox'
    i_am_ready_to_begin_btn = AppiumBy.ID, 'com.embibe.student:id/btn_ready'
    old_test_ui_start_test_btn = AppiumBy.ID, 'com.embibe.student:id/btn_start'
    submit_btn = AppiumBy.ID, 'com.embibe.student:id/btnSubmitTest'
    submit_confirm_btn = AppiumBy.ID, 'com.embibe.student:id/btnSubmitTest'
    view_fb_btn = AppiumBy.ID, 'com.embibe.student:id/btnContinueTest'
    trending_test_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Trending Tests for Your Exam"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    full_test_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Take Full Tests"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    chapter_test_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Take Chapter Tests"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    recommended_learning_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Recommended Learning to Ace this Test"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    recommended_practice_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Recommended Practice to Ace this Test"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    more_tests = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="More Tests on this Syllabus"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    video_resume_button = AppiumBy.ID, 'com.embibe.student:id/btn_resume'
    video_close_button = AppiumBy.ID, 'com.embibe.student:id/btn_quit'
    practice_milestone = AppiumBy.XPATH, '//android.widget.Image[@text="milestone-active"]'
    practice_close_btn = By.XPATH, '//android.widget.TextView[@text=""]'

    def five_mins_custom_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        # ScrollUtil.scrollToTextByAndroidUIAutomator('My Custom Tests', self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.custom_test_tile)
        self.driver.find_element(*TestHome.custom_test_tile).click()
        sub_count = self.driver.find_elements(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.embibe.student:id/rv_subjects"]/(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_root"])')
        print(len(sub_count))
        for i in range(1, len(sub_count)+1):
            self.driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.embibe.student:id/rv_subjects"]/(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_root"])['+str(i)+']').click()

        self.driver.find_element(*TestHome.continue_btn).click()
        time.sleep(3)

        for j in range (1, len(sub_count)+1):
            self.driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_subject_root"])['+str(j)+']').click()
            # time.sleep(2)
            self.driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_chapter_row_root"])[1]').click()
            # time.sleep(2)
            self.driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_subject_root"])['+str(j)+']').click()
            # time.sleep(2)

        self.driver.find_element(*TestHome.quick_5_min_test_btn).click()
        time.sleep(10)
        self.test_taking()

        self.driver.press_keycode(4)

        # Recommended Learning to Ace this Test
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.recommended_learning_tile)
        self.driver.find_element(*TestHome.recommended_learning_tile).click()
        time.sleep(3)
        self.video_details()

        # Recommended Practice to Ace this Test
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.recommended_practice_tile)
        self.driver.find_element(*TestHome.recommended_practice_tile).click()
        time.sleep(10)

        # self.driver.find_element(*TestHome.practice_milestone).is_displayed()
        self.practice_taking()


    def custom_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        # ScrollUtil.scrollToTextByAndroidUIAutomator('My Custom Tests', self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.custom_test_tile)
        self.driver.find_element(*TestHome.custom_test_tile).click()
        sub_count = self.driver.find_elements(AppiumBy.XPATH,
                                              '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.embibe.student:id/rv_subjects"]/(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_root"])')
        print(len(sub_count))
        for i in range(1, len(sub_count) + 1):
            self.driver.find_element(AppiumBy.XPATH,
                                     '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.embibe.student:id/rv_subjects"]/(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_root"])[' + str(
                                         i) + ']').click()

        self.driver.find_element(*TestHome.continue_btn).click()
        time.sleep(3)

        for j in range(1, len(sub_count) + 1):
            self.driver.find_element(AppiumBy.XPATH,
                                     '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_subject_root"])[' + str(
                                         j) + ']').click()
            # time.sleep(2)
            self.driver.find_element(AppiumBy.XPATH,
                                     '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_chapter_row_root"])[1]').click()
            # time.sleep(2)
            self.driver.find_element(AppiumBy.XPATH,
                                     '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_subject_root"])[' + str(
                                         j) + ']').click()
            # time.sleep(2)

        self.driver.find_element(*TestHome.custom_test_btn).click()
        self.driver.find_element(*TestHome.test_name_field).send_keys('Custom Test')
        self.driver.find_element(*TestHome.create_test_btn).click()
        time.sleep(20)

        self.test_taking()

        self.driver.press_keycode(4)

        # Recommended Learning to Ace this Test
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.recommended_learning_tile)
        self.driver.find_element(*TestHome.recommended_learning_tile).click()
        time.sleep(3)
        self.video_details()

        # Recommended Practice to Ace this Test
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.recommended_practice_tile)
        self.driver.find_element(*TestHome.recommended_practice_tile).click()
        time.sleep(10)

        # self.driver.find_element(*TestHome.practice_milestone).is_displayed()
        self.practice_taking()

    def trending_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        time.sleep(5)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Trending Tests for Your Exam', self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.trending_test_tile)
        time.sleep(5)
        self.driver.find_element(*TestHome.trending_test_tile).click()
        self.test_taking()

        self.driver.press_keycode(4)

        #Recommended Learning to Ace this Test
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.recommended_learning_tile)
        self.driver.find_element(*TestHome.recommended_learning_tile).click()
        time.sleep(3)
        self.video_details()


        # Recommended Practice to Ace this Test
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.recommended_practice_tile)
        self.driver.find_element(*TestHome.recommended_practice_tile).click()
        time.sleep(10)

        # self.driver.find_element(*TestHome.practice_milestone).is_displayed()
        self.practice_taking()


        # More Tests
        # ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.more_tests)
        # self.driver.find_element(*TestHome.more_tests).click()
        # try:
        #     popup_element = self.driver.find_element(*TestHome.test_env_popup)
        #     if popup_element.is_displayed():
        #         self.driver.find_element(*TestHome.sel_new_embibe_expUI).click()
        #         self.driver.find_element(*TestHome.instruc_next_button).click()
        #         self.driver.find_element(*TestHome.instruct_chkbox).click()
        #         self.driver.find_element(*TestHome.i_am_ready_to_begin_btn).click()
        #         time.sleep(5)
        #
        #     else:
        #         self.driver.find_element(*TestHome.instruct_chkbox).click()
        #         self.driver.find_element(*TestHome.old_test_ui_start_test_btn).click()
        #         time.sleep(5)
        #
        # except NoSuchElementException:
        #     print("Test Feedback")
        #     time.sleep(5)



    def full_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        time.sleep(5)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Take Full Tests', self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.full_test_tile)
        self.driver.find_element(*TestHome.full_test_tile).click()
        self.test_taking()
        self.driver.press_keycode(4)

        # Recommended Learning to Ace this Test
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.recommended_learning_tile)
        self.driver.find_element(*TestHome.recommended_learning_tile).click()
        time.sleep(3)
        self.video_details()

        # Recommended Practice to Ace this Test
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.recommended_practice_tile)
        self.driver.find_element(*TestHome.recommended_practice_tile).click()
        time.sleep(10)

        # self.driver.find_element(*TestHome.practice_milestone).is_displayed()
        self.practice_taking()

    def chapter_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        time.sleep(5)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Take Chapter Tests', self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.chapter_test_tile)

        self.driver.find_element(*TestHome.chapter_test_tile).click()
        self.test_taking()
        self.driver.press_keycode(4)

        # Recommended Learning to Ace this Test
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.recommended_learning_tile)
        self.driver.find_element(*TestHome.recommended_learning_tile).click()
        time.sleep(3)
        self.video_details()

        # Recommended Practice to Ace this Test
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.recommended_practice_tile)
        self.driver.find_element(*TestHome.recommended_practice_tile).click()
        time.sleep(10)

        # self.driver.find_element(*TestHome.practice_milestone).is_displayed()
        self.practice_taking()



    def test_taking(self):
        try:
            btn = self.driver.find_element(*TestHome.test_btn).text

            if btn == 'Start Test':
                self.driver.find_element(*TestHome.test_btn).click()
                try:
                    popup_element = self.driver.find_element(*TestHome.test_env_popup)
                    if popup_element.is_displayed():
                        self.driver.find_element(*TestHome.sel_new_embibe_expUI).click()
                        self.driver.find_element(*TestHome.instruc_next_button).click()
                        self.driver.find_element(*TestHome.instruct_chkbox).click()
                        self.driver.find_element(*TestHome.i_am_ready_to_begin_btn).click()
                except NoSuchElementException:
                    self.driver.find_element(*TestHome.instruct_chkbox).click()
                    self.driver.find_element(*TestHome.old_test_ui_start_test_btn).click()

            elif btn == 'Expired':
                print("Test has been Expired")

            elif btn == 'Resume Test':
                self.driver.find_element(*TestHome.test_btn).click()

            time.sleep(10)
            # ele = self.driver.find_elements(AppiumBy.XPATH, "//div[@class='test-wrapper ']/div/div[2]/div[1]/button")
            # for k in range(1, len(ele) + 1):
            #     self.driver.find_element(AppiumBy.XPATH, "//div[@class='test-wrapper ']/div/div[2]/div[1]/button[" + str(
            #         k) + "]").click()
            #     questions = self.driver.find_elements(*TestHomePage.question_count)
            #     for i in range(1, len(questions)):
            #         time.sleep(3)
            #         question = self.driver.find_element(*TestHomePage.question_type).text
            #
            #         if question in ['Single Choice', 'Multiple Choice', 'True-False']:
            #             try:
            #
            #                 self.driver.find_element(*TestHomePage.option_A_click).click()
            #                 self.driver.find_element(*TestHomePage.save_next_btn).click()
            #             except NoSuchElementException:
            #                 self.driver.find_element(*TestHomePage.save_next_btn).click()
            #
            #         elif question == 'Subjective Answer':
            #             try:
            #
            #                 self.driver.find_element(*TestHomePage.sub_input_field).click()
            #                 self.driver.find_element(*TestHomePage.sub_input_field).send_keys("XYZ")
            #                 self.driver.find_element(*TestHomePage.save_next_btn).click()
            #             except NoSuchElementException:
            #                 self.driver.find_element(*TestHomePage.save_next_btn).click()
            #
            #         elif question == 'Subjective Numerical':
            #             try:
            #
            #                 self.driver.find_element(*TestHomePage.sub_input_field).click()
            #                 self.driver.find_element(*TestHomePage.sub_input_field).send_keys("123")
            #                 self.driver.find_element(*TestHomePage.save_next_btn).click()
            #             except NoSuchElementException:
            #                 self.driver.find_element(*TestHomePage.save_next_btn).click()
            #
            #         elif question == 'Fill in The Blanks':
            #             try:
            #
            #                 self.driver.find_element(*TestHomePage.fib_1_field).click()
            #                 self.driver.find_element(*TestHomePage.fib_1_field).send_keys("XYZ")
            #                 self.driver.find_element(*TestHomePage.save_next_btn).click()
            #             except NoSuchElementException:
            #                 self.driver.find_element(*TestHomePage.save_next_btn).click()
            #
            #         elif question == 'Matrix':
            #             try:
            #
            #                 self.driver.find_element(*TestHomePage.save_next_btn).click()
            #             except NoSuchElementException:
            #                 self.driver.find_element(*TestHomePage.save_next_btn).click()
            #
            #         elif question == 'Multiple Fill in The Blanks':
            #             try:
            #
            #                 self.driver.find_element(*TestHomePage.fib_1_field).click()
            #                 self.driver.find_element(*TestHomePage.fib_2_field).click()
            #                 self.driver.find_element(*TestHomePage.save_next_btn).click()
            #             except NoSuchElementException:
            #                 self.driver.find_element(*TestHomePage.save_next_btn).click()
            #
            #         else:
            #             self.driver.find_element(*TestHomePage.save_next_btn).click()

            self.driver.find_element(*TestHome.submit_btn).click()
            time.sleep(5)
            self.driver.find_element(*TestHome.submit_confirm_btn).click()
            time.sleep(5)
            self.driver.find_element(*TestHome.view_fb_btn).click()
            time.sleep(15)
            # assert "Predicted Improvement" == self.driver.find_element("//*[contains(text(),'Predicted')]").text

        except Exception as e:
            if btn == 'View Test Feedback':
                print("Test already Taken")
            else:
                print(f"An error occurred: {e}")

    def video_details(self):
        try:
            if self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*TestHome.video_resume_button).click()
                time.sleep(3)
                self.driver.press_keycode(4)
                self.driver.find_element(*TestHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(3)
            self.driver.press_keycode(4)
            self.driver.find_element(*TestHome.video_close_button).click()


    def practice_taking(self):
        time.sleep(10)

        for i in range(1, 4):
            try:
                time.sleep(3)
                question_element = self.driver.find_element(AppiumBy.XPATH,
                                                       '//android.view.View[@resource-id="PracticeConatiner"]/android.view.View/android.widget.TextView[1]').text
                print(question_element)

                if "Multiple Choice" in question_element:
                    time.sleep(5)

                    self.driver.find_element(AppiumBy.XPATH,
                                        '//android.view.View[@resource-id="PracticeConatiner"]/android.view.View[1]/android.view.View[3]').click()

                    self.driver.find_element(AppiumBy.XPATH,
                                        '//android.view.View[@resource-id="PracticeConatiner"]/android.view.View[1]/android.view.View[4]').click()
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Check\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

                elif "Single Choice" in question_element:
                    time.sleep(3)
                    self.driver.find_element(AppiumBy.XPATH,
                                        "//android.view.View[@resource-id=\"PracticeConatiner\"]/android.view.View[1]/android.view.View[4]").click()
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Check\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

                elif "True-False" in question_element:
                    time.sleep(3)
                    self.driver.find_element(AppiumBy.XPATH,
                                        '//android.view.View[@resource-id="PracticeConatiner"]/android.view.View[1]/android.view.View[4]').click()
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Check\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

                elif "Assertion" in question_element:
                    time.sleep(3)
                    self.driver.find_element(AppiumBy.XPATH,
                                        '//android.view.View[@resource-id="PracticeConatiner"]/android.view.View[1]/android.view.View[2]').click()
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Check\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()


                elif "Single DropDown" in question_element:
                    time.sleep(3)
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Select\")").click()
                    time.sleep(2)
                    self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.TextView[@text="Select"]/parent::android.view.View/parent::android.view.View/android.view.View[2]/android.view.View/android.widget.TextView[1]').click()
                    time.sleep(2)
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Check\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

                elif "Subjective" in question_element:
                    # self.driver.find_element(By.XPATH,
                    #                     "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()

                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                        value="new UiSelector().text(\"Full Solution\")").click()
                    time.sleep(10)

                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()


                elif "Subjective Numerical" in question_element:
                    time.sleep(5)
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                        value="new UiSelector().text(\"Solve With Us\")").click()
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                        value="new UiSelector().text(\"Full Solution\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

                elif "Subjective Answer" in question_element:
                    time.sleep(5)
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                        value="new UiSelector().text(\"Solve With Us\")").click()
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                        value="new UiSelector().text(\"Full Solution\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()


                elif "Fill in The Blanks" in question_element:
                    time.sleep(3)
                    self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@resource-id=\"fb-blank-0\"]").click()
                    self.driver.find_element(AppiumBy.XPATH,
                                        '//android.view.View[@resource-id="fb-blank-0"]/android.widget.EditText').send_keys(
                        "abc")
                    self.driver.hide_keyboard()
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Check"]').click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

                elif "Integer" in question_element:
                    time.sleep(3)
                    self.driver.find_element(AppiumBy.XPATH,
                                        "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()
                    self.driver.find_element(AppiumBy.CSS_SELECTOR, "[id='fb-blank-0']").click()
                    time.sleep(2)

                    self.driver.find_element(AppiumBy.CSS_SELECTOR, "[status='DEFAULT']").send_keys("1")
                    time.sleep(2)
                    self.driver.find_element(AppiumBy.XPATH, "//*[@text='Check']").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, "//*[@text='Continue']").click()

                elif "Multiple Fill in The Blanks" in question_element:
                    self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="fb-blank-0"]').click()
                    time.sleep(2)
                    self.driver.find_element(AppiumBy.XPATH,
                                        '//android.view.View[@resource-id="fb-blank-0"]/android.widget.EditText').send_keys(
                        "abc")
                    self.driver.hide_keyboard()

                    self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="fb-blank-1"]').click()
                    time.sleep(2)
                    self.driver.find_element(AppiumBy.XPATH,
                                        '//android.view.View[@resource-id="fb-blank-1"]/android.widget.EditText').send_keys(
                        "xyz")
                    self.driver.hide_keyboard()

                    self.driver.find_element(AppiumBy.XPATH, "//*[@text='Check']").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, "//*[@text='Continue']").click()

                    # driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text=\"Solve With Us\"]").click()
                    # driver.find_element(AppiumBy.XPATH, "//*[@text='Full Solution']").click()
                    # driver.find_element(AppiumBy.XPATH, "//*[@text='Continue']").click()

                elif "Learn Intervention" in question_element:
                    self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text=\"Continue Practice\"]").click()

            except NoSuchElementException:
                self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text=\"Solve With Us\"]").click()
                self.driver.find_element(AppiumBy.XPATH, "//*[@text='Full Solution']").click()
                self.driver.find_element(AppiumBy.XPATH, "//*[@text='Continue']").click()

        self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text=""]').click()
        self.driver.find_element(AppiumBy.ID, 'com.embibe.student:id/btn_quit').click()


