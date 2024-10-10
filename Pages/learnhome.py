import time
from appium.webdriver.common.appiumby import AppiumBy

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains

from Utilities import scroll_util
from Utilities.scroll_util import ScrollUtil


class LearnHome:

    def __init__(self, driver):
        self.driver=driver

    continue_learning_tile =  AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Continue Learning"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    guided_tour_next_btn = AppiumBy.ID, 'com.embibe.student:id/tvNext'
    guided_tour_cancel_btn = AppiumBy.ID, 'com.embibe.student:id/ivClose'
    home_tab = AppiumBy.ID, 'com.embibe.student:id/navigation_home'
    practice_tab = AppiumBy.ID, 'com.embibe.student:id/navigation_practice'
    test_tab = AppiumBy.ID, 'com.embibe.student:id/navigation_test'
    achieve_tab = AppiumBy.ID, 'com.embibe.student:id/navigation_achieve'
    learn_tab = AppiumBy.ID, 'com.embibe.student:id/navigation_learn'
    trending_videos_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Trending Videos for Your Exam"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    bookmark_button = AppiumBy.ID, 'com.embibe.student:id/bookmark'
    download_button = AppiumBy.ID, 'com.embibe.student:id/fl_download_container'
    video_close_button = AppiumBy.ID, 'com.embibe.student:id/btn_quit'
    video_resume_button = AppiumBy.ID, 'com.embibe.student:id/btn_resume'
    video_play_button = AppiumBy.ID, 'com.embibe.student:id/ivSummaryHeroBannerPlay1'
    more_topic_tile = AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.embibe.student:id/imgBanner"])[2]'
    related_video_tile = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/adBannerCardView"])[4]'
    embibe_explainer_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Embibe Explainers"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    books_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Books With Videos & Solutions"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    add_book_button = AppiumBy.ID, 'com.embibe.student:id/btn_myBooks'
    book_chapter_button = AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/clBookChapter"])[1]'
    book_topic_button = AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.embibe.student:id/ll_topic"])[1]'
    book_practice_chapter_tile = AppiumBy.ID, 'com.embibe.student:id/thumbPracticeForChapterIV'
    book_practice_topic_tile = AppiumBy.ID, 'com.embibe.student:id/thumbPracticeForChapterIV'
    practice_quit_button = AppiumBy.ID, 'com.embibe.student:id/btn_quit'
    learn_chapter_tile = AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.embibe.student:id/header\" and contains(@text, 'Chapters From')]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]"
    learn_button = AppiumBy.ID, 'com.embibe.student:id/tvSummaryLearnButton'
    sincerity_score_tile = AppiumBy.ID, 'com.embibe.student:id/ivSincerityScorePlay'
    sincerity_score_close_btn = AppiumBy.ID, 'com.embibe.student:id/btn_quit'
    learn_PTR = AppiumBy.ID, 'com.embibe.student:id/clFullTileCheatSheet'
    topics_in_this_chapter = AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.embibe.student:id/llTile"])[1]'
    embibe_explainers = AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.embibe.student:id/imgBanner"])[3]'
    prerequisite_topics_videos = AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.embibe.student:id/imgBanner"])[4]'

    def guided_tour(self):
        for i in range(1,6):
            self.driver.find_element(*LearnHome.guided_tour_next_btn).click()

    def module_click(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*LearnHome.home_tab).click()
        home_car = self.driver.find_element(AppiumBy.XPATH, '//android.widget.RelativeLayout[@resource-id="com.embibe.student:id/headingSectionParentView"]').text
        home_car== 'Assignment from My Parents'
        time.sleep(3)

        self.driver.find_element(*LearnHome.practice_tab).click()
        # prac_car = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.RelativeLayout[@resource-id="com.embibe.student:id/headingSectionParentView"])[3]').text
        # time.sleep(3)
        # assert 'Adaptive Practice' in prac_car

        self.driver.find_element(*LearnHome.test_tab).click()
        time.sleep(3)


        self.driver.find_element(*LearnHome.achieve_tab).click()
        time.sleep(3)
        # achieve_car = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Explore Mastery"]').text
        # assert 'Explore Mastery' in achieve_car

        self.driver.find_element(*LearnHome.learn_tab).click()
        time.sleep(3)
        learn_car = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.RelativeLayout[@resource-id="com.embibe.student:id/headingSectionParentView"])[2]').text
        'Live Class' in learn_car


    def trending_videos(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Trending Videos for Your Exam', self.driver)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Trending Videos for Your Exam', self.driver)
        # ScrollUtil.swipeUp(2,self.driver)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Trending Videos for Your Exam', self.driver)
        # time.sleep(5)
        # self.driver.find_element(*LearnHome.trending_videos_tile).click()
        # self.video_details()

        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.trending_videos_tile)
        self.driver.find_element(*LearnHome.trending_videos_tile).click()
        self.video_details()







    def embibe_explainer_videos(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(5)
        # ScrollUtil.swipeUp(2, self.driver)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Embibe Explainers', self.driver)
        # time.sleep(5)
        # self.driver.find_element(*LearnHome.embibe_explainer_tile).click()
        # self.video_details()
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.embibe_explainer_tile)
        self.driver.find_element(*LearnHome.embibe_explainer_tile).click()
        self.video_details()

    def books_with_videos_solutions(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(5)
        # ScrollUtil.swipeUp(2, self.driver)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Books With Videos & Solution', self.driver)
        # time.sleep(5)
        # self.driver.find_element(*LearnHome.books_tile).click()
        # self.driver.find_element(*LearnHome.add_book_button).click()

        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.books_tile)
        self.driver.find_element(*LearnHome.books_tile).click()
        self.video_details()

    def learn_chapters(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.learn_chapter_tile)
        time.sleep(5)
        self.driver.find_element(*LearnHome.learn_chapter_tile).click()
        self.driver.find_element(*LearnHome.learn_button).click()
        try:
            if self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()
            time.sleep(3)

        # PTR
        self.driver.find_element(*LearnHome.learn_PTR).click()
        time.sleep(5)
        self.driver.press_keycode(4)

        #Sincerity Score
        self.driver.find_element(*LearnHome.sincerity_score_tile).click()
        time.sleep(3)
        self.driver.press_keycode(4)
        self.driver.find_element(*LearnHome.sincerity_score_close_btn).click()
        time.sleep(3)


        ScrollUtil.swipeUp(1, self.driver)

        # Embibe Explainers
        self.driver.find_element(*LearnHome.embibe_explainers).click()
        try:
            if self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
                time.sleep(3)
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()
            time.sleep(3)



        # Topics in this chapter
        self.driver.find_element(*LearnHome.topics_in_this_chapter).click()
        self.driver.find_element(*LearnHome.learn_button).click()
        try:
            if self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()
            time.sleep(3)
        self.driver.press_keycode(4)

        #Prerequisite Topics
        ScrollUtil.swipeUp(4, self.driver)
        time.sleep(2)

        self.driver.find_element(*LearnHome.prerequisite_topics_videos).click()
        self.driver.find_element(*LearnHome.learn_button).click()
        try:
            if self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()
            time.sleep(3)
        self.driver.press_keycode(4)
        ScrollUtil.swipeUp(4, self.driver)
        time.sleep(2)

    def continue_learning(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(5)
        # ScrollUtil.swipeUp(2, self.driver)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Continue Learning',self.driver)
        # self.driver.find_element(*LearnHome.continue_learning_tile).click()
        # self.video_details()

        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.continue_learning_tile)
        self.driver.find_element(*LearnHome.continue_learning_tile).click()
        self.video_details()

    def video_details(self):
        self.driver.find_element(*LearnHome.bookmark_button).click()
        # self.driver.find_element(*LearnHome.download_button).click()
        self.driver.find_element(*LearnHome.video_play_button).click()
        time.sleep(2)
        try:
            if self.driver.find_element(AppiumBy.ID, 'com.embibe.student:id/btn_resume').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()


        #More Topic Video Click
        self.driver.find_element(*LearnHome.more_topic_tile).click()
        try:
            if self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()

        #Related Video Click
        time.sleep(2)
        self.driver.find_element(*LearnHome.related_video_tile).click()
        try:
            if self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()


