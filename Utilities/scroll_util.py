from appium.webdriver.common.appiumby import AppiumBy


class ScrollUtil:

    @staticmethod
    def scrollToTextByAndroidUIAutomator(text,driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,("new UiScrollable(new UiSelector().scrollable(true).instance("
                                                   "0)).scrollIntoView(new UiSelector().textContains(\""+text+"\").instance(0))"))

    @staticmethod
    def swipeUp(howManySwipes,driver):
        for i in range(1,howManySwipes+1):
            driver.swipe(400, 1125, 400, 200, 1000)

    @staticmethod
    def swipeDown(howManySwipes,driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(514, 500, 514, 800, 1000)

    @staticmethod
    def swipeLeft(howManySwipes,driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(900, 600, 200, 600, 1000)

    @staticmethod
    def swipeRight(howManySwipes,driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(200, 600, 900, 600, 1000)


    @staticmethod
    def scroll_until_element_is_visible(driver, locator, action=None, max_scrolls=10):
        """
        Scroll the page until the element specified by 'locator' is visible.

        :param locator: The locator tuple (By, value) for the target element.
        :param action: Optional action (e.g., click) to perform when the element is found.
        :param max_scrolls: Maximum number of scroll attempts before giving up.
        :return: True if the element is found and the action is performed, False otherwise.
        """
        scrolls = 0

        while scrolls < max_scrolls:
            try:
                # Try to locate the element
                elements = driver.find_elements(*locator)  # Using find_elements to avoid exceptions
                if elements:  # Check if elements list is not empty
                    if elements[0].is_displayed():
                        # If it's displayed, perform the action (if any) and return
                        if action:
                            action(elements[0])  # Perform the passed action
                        return True
            except Exception as e:
                # Handle exceptions, log and continue scrolling
                print(f"Scroll {scrolls + 1}: Element not found, swiping up. Exception: {str(e)}")

            # Perform scroll action
            ScrollUtil.swipeUp(1, driver)
            scrolls += 1

        # If the element is not found after maximum scrolls, return False
        print(f"Max scrolls reached. Element not found using locator: {locator}")
        return False