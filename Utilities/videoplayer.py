import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException


class videoplayer:

    def __init__(self):
        def __init__(self, driver):
            self.driver = driver

        bookmark_button = AppiumBy.ID, 'com.embibe.student:id/bookmark'
        download_button = AppiumBy.ID, 'com.embibe.student:id/fl_download_container'
        video_close_button = AppiumBy.ID, 'com.embibe.student:id/btn_quit'
        video_resume_button = AppiumBy.ID, 'com.embibe.student:id/btn_resume'
        video_play_button = AppiumBy.ID, 'com.embibe.student:id/ivSummaryHeroBannerPlay1'
        more_topic_tile = AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.embibe.student:id/imgBanner"])[2]'
        related_video_tile = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/adBannerCardView"])[4]'

