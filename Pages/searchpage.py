import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException


class Search_Module:

    def __init__(self, driver):
        self.driver=driver

    search_btn = AppiumBy.ID, 'com.embibe.student:id/search'
    search_field = AppiumBy.ID, 'com.embibe.student:id/query'
    result_tile = AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.embibe.student:id/imgBanner"])[1]'
    learn_tab = AppiumBy.XPATH, '//android.widget.TextView[@text="Learn"]'
    books_tab = AppiumBy.XPATH, '//android.widget.TextView[@text="Books"]'
    questions_tab = AppiumBy.XPATH, '//android.widget.TextView[@text="Questions"]'
    questions_tile = AppiumBy.ID, 'com.embibe.student:id/questionCL'
    practice_tab = AppiumBy.XPATH, '//android.widget.TextView[@text="Practice"]'
    test_tab = AppiumBy.XPATH, '//android.widget.TextView[@text="Test"]'
    ptr_tab = AppiumBy.XPATH, '//android.widget.TextView[@text="Points to Remember"]'
    guided_tour_cancel_btn = AppiumBy.ID, 'com.embibe.student:id/ivClose'
    home_tab = AppiumBy.ID, 'com.embibe.student:id/navigation_home'
    bookmark_button = AppiumBy.ID, 'com.embibe.student:id/bookmark'
    download_button = AppiumBy.ID, 'com.embibe.student:id/fl_download_container'
    video_close_button = AppiumBy.ID, 'com.embibe.student:id/btn_quit'
    video_resume_button = AppiumBy.ID, 'com.embibe.student:id/btn_resume'
    change_goal_popup = AppiumBy.ID, 'com.embibe.student:id/do_u_want_view_TV'
    update_goal_btn = AppiumBy.ID, 'com.embibe.student:id/upgrade_goal_TV'
    practice_milestone = AppiumBy.XPATH, '//android.widget.Image[@text="milestone-active"]'
    book_chapter = AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/clBookChapter"])[1]'
    book_topic_video = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/adBannerCardView"])[1]'
    book_practice_tile = AppiumBy.ID , 'com.embibe.student:id/thumbPracticeForChapterIV'
    book_ptr_tile =  AppiumBy.ID, 'com.embibe.student:id/thumbCheatSheet'
    share_button = AppiumBy.ID, 'com.embibe.student:id/ivShare'
    test_env_popup = AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_parent_close_video"]/android.view.ViewGroup'
    test_env_continue_btn = AppiumBy.ID, 'com.embibe.student:id/btn_continue'
    test_instru_next_btn = AppiumBy.ID, 'com.embibe.student:id/btn_next'
    test_instru_checkbox_btn = AppiumBy.ID, 'com.embibe.student:id/iv_checkbox'
    test_i_am_ready_to_begin_btn = AppiumBy.ID, 'com.embibe.student:id/btn_ready'
    test_old_ui_start_now_btn = AppiumBy.ID, 'com.embibe.student:id/btn_start'
    test_fb_achieve_btn = AppiumBy.ID, 'com.embibe.student:id/tv_continue_learning'

    def search_module_click(self):
        self.driver.find_element(*Search_Module.guided_tour_cancel_btn).click()
        self.driver.find_element(*Search_Module.home_tab).click()
        time.sleep(5)
        self.driver.find_element(*Search_Module.search_btn).click()
        time.sleep(2)
        self.driver.find_element(*Search_Module.search_field).send_keys("Magnetic Current")
        self.driver.press_keycode(66)
        self.driver.find_element(*Search_Module.learn_tab).click()
        self.driver.find_element(*Search_Module.books_tab).click()
        self.driver.find_element(*Search_Module.practice_tab).click()
        self.driver.find_element(*Search_Module.questions_tab).click()
        self.driver.find_element(*Search_Module.test_tab).click()
        self.driver.find_element(*Search_Module.ptr_tab).click()

    def search_learn_video_click(self):

            self.driver.find_element(*Search_Module.guided_tour_cancel_btn).click()
            time.sleep(10)
            self.driver.find_element(*Search_Module.search_btn).click()
            time.sleep(2)
            self.driver.find_element(*Search_Module.search_field).send_keys("Magnetic Current")
            self.driver.press_keycode(66)
            self.driver.find_element(*Search_Module.learn_tab).click()
            self.driver.find_element(*Search_Module.result_tile).click()
            self.video_details()

    def search_practice_click(self):
        self.driver.find_element(*Search_Module.guided_tour_cancel_btn).click()
        time.sleep(10)
        self.driver.find_element(*Search_Module.search_btn).click()
        time.sleep(2)
        self.driver.find_element(*Search_Module.search_field).send_keys("Magnetic Current")
        self.driver.press_keycode(66)
        self.driver.find_element(*Search_Module.practice_tab).click()
        self.driver.find_element(*Search_Module.result_tile).click()
        time.sleep(2)
        try:
            # Check if the exam change popup is displayed and click if found
            if self.driver.find_element(*Search_Module.change_goal_popup).is_displayed():
                self.driver.find_element(*Search_Module.update_goal_btn).click()
                time.sleep(10)  # Wait for the next element to appear

            # Check if the practice milestone is displayed
            self.driver.find_element(*Search_Module.practice_milestone).is_displayed()

        except Exception as e:
            # Handle the exception and still check for the practice milestone
            time.sleep(10)
            self.driver.find_element(*Search_Module.practice_milestone).is_displayed()

    def search_question_click(self):
        self.driver.find_element(*Search_Module.guided_tour_cancel_btn).click()
        time.sleep(10)
        self.driver.find_element(*Search_Module.search_btn).click()
        time.sleep(2)
        self.driver.find_element(*Search_Module.search_field).send_keys("Magnetic Current")
        self.driver.press_keycode(66)
        self.driver.find_element(*Search_Module.questions_tab).click()
        self.driver.find_element(*Search_Module.questions_tile).click()
        time.sleep(5)
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="First Looked"]').is_displayed()

    def search_book_click(self):
        self.driver.find_element(*Search_Module.guided_tour_cancel_btn).click()
        time.sleep(10)
        self.driver.find_element(*Search_Module.search_btn).click()
        time.sleep(2)
        self.driver.find_element(*Search_Module.search_field).send_keys("Magnetic Current")
        self.driver.press_keycode(66)
        self.driver.find_element(*Search_Module.books_tab).click()
        self.driver.find_element(*Search_Module.result_tile).click()
        time.sleep(4)
        self.driver.find_element(*Search_Module.share_button).is_displayed()

        #Chapter and Topic Click
        # time.sleep(5)
        # self.driver.find_element(*Search_Module.book_chapter).click()
        # self.driver.find_element(*Search_Module.book_practice_tile).click()
        # time.sleep(5)
        # self.driver.find_element(*Search_Module.practice_milestone).is_displayed()
        # self.driver.press_keycode(4)
        # self.driver.find_element(AppiumBy.ID, 'com.embibe.student:id/btn_quit').click()
        # time.sleep(5)
        # self.driver.find_element(*Search_Module.book_ptr_tile).click()
        # self.driver.find_element(*Search_Module.book_chapter).click()
        # self.driver.find_element(*Search_Module.book_topic_video).click()
        # self.video_details()
        #

    def search_PTR_click(self):
        self.driver.find_element(*Search_Module.guided_tour_cancel_btn).click()
        time.sleep(10)
        self.driver.find_element(*Search_Module.search_btn).click()
        time.sleep(2)
        self.driver.find_element(*Search_Module.search_field).send_keys("Magnetic Current")
        self.driver.press_keycode(66)
        self.driver.find_element(*Search_Module.practice_tab).click()
        self.driver.find_element(*Search_Module.ptr_tab).click()
        self.driver.find_element(*Search_Module.result_tile).click()
        time.sleep(5)

    def search_test_and_click(self):
        # Cancel the guided tour if the button is displayed
        self.driver.find_element(*Search_Module.guided_tour_cancel_btn).click()
        time.sleep(10)

        # Perform search for "Current"
        self.driver.find_element(*Search_Module.search_btn).click()
        time.sleep(2)
        self.driver.find_element(*Search_Module.search_field).send_keys("life processes")
        self.driver.press_keycode(66)

        # Navigate through tabs and select the result tile
        self.driver.find_element(*Search_Module.practice_tab).click()
        self.driver.find_element(*Search_Module.test_tab).click()
        self.driver.find_element(*Search_Module.result_tile).click()
        time.sleep(2)

        try:
        # Check if the goal change popup is displayed
            if self.driver.find_element(*Search_Module.change_goal_popup).is_displayed():
                self.driver.find_element(*Search_Module.update_goal_btn).click()
                if self.driver.find_element(*Search_Module.test_env_popup).is_displayed():
                    self.driver.find_element(*Search_Module.test_env_continue_btn).click()
                    self.driver.find_element(*Search_Module.test_instru_next_btn).click()
                    self.driver.find_element(*Search_Module.test_instru_checkbox_btn).click()
                    self.driver.find_element(*Search_Module.test_i_am_ready_to_begin_btn).click()

                elif self.driver.find_element(*Search_Module.test_instru_checkbox_btn).is_displayed():
                    self.driver.find_element(*Search_Module.test_instru_checkbox_btn).click()
                    self.driver.find_element(*Search_Module.test_i_am_ready_to_begin_btn).click()

        # Fallback: Check if the Facebook achievement button is displayed
                else:
                    self.driver.find_element(*Search_Module.test_fb_achieve_btn).is_displayed()

        except NoSuchElementException:
            # Fallback: Handle exception for missing elements
            if self.driver.find_element(*Search_Module.test_instru_checkbox_btn).is_displayed():
               self.driver.find_element(*Search_Module.test_instru_checkbox_btn).click()
               self.driver.find_element(*Search_Module.test_old_ui_start_now_btn).click()

        # Handle the test environment popup in case of exception
            elif self.driver.find_element(*Search_Module.test_env_popup).is_displayed():
                self.driver.find_element(*Search_Module.test_env_continue_btn).click()
                self.driver.find_element(*Search_Module.test_instru_next_btn).click()
                self.driver.find_element(*Search_Module.test_instru_checkbox_btn).click()
                self.driver.find_element(*Search_Module.test_i_am_ready_to_begin_btn).click()

        # Fallback: Check if the Facebook achievement button is displayed
            else:
                self.driver.find_element(*Search_Module.test_fb_achieve_btn).is_displayed()

    def video_details(self):
        try:
            if self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*Search_Module.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*Search_Module.video_close_button).click()
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*Search_Module.video_close_button).click()




