import time

import pytest
from Pages.landingPages import landingpages
from Pages.profile_menu import Profile_Menu
from Pages.searchpage import Search_Module
from Pages.learnhome import LearnHome
from Pages.testhome import TestHome
from Pages.userhome import UserHome
from Testcases.Baseclass import BaseClass


class TestEmbibeApp(BaseClass):

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def _login_with_password(self):
        lp = landingpages(self.driver)
        lp.signinusingpassword()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_login_with_password(self):
        self._login_with_password()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_login_with_OTP(self):
        lp = landingpages(self.driver)
        lp.signinusingOTP()
        # log = self.getLogger()
        # log.info("Testcase 2 : User Logs in via OTP")

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_forgot_password(self):
        lp = landingpages(self.driver)
        lp.clickforgotpassword()
        # log = self.getLogger()
        # log.info("Testcase 3 : User clicks Forgot Password")

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_click_tos(self):
        lp = landingpages(self.driver)
        lp.clickTOS()
        # log = self.getLogger()
        # log.info("Testcase 4: User clicks on Terms and Conditions link")

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_click_PP(self):
        lp = landingpages(self.driver)
        lp.clickPrivacyPolicy()
        # log = self.getLogger()
        # log.info("Testcase 5: User clicks on Privacy Policy link")

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_tos_in_signinpage(self):
        lp = landingpages(self.driver)
        lp.tosinsigninpage()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_privacy_policy_in_signinpage(self):
        lp = landingpages(self.driver)
        lp.privacypolicyinsigninpage()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_guided_tour(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.guided_tour()
        time.sleep(2)

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_module_click(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.module_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_trending_video_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.trending_videos()
    #
    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_embibe_explainer_video_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.embibe_explainer_videos()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_books_with_videos_solutions_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.books_with_videos_solutions()


    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_learn_chapter_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.learn_chapters()
        time.sleep(3)

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_continue_learning_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.continue_learning()
        time.sleep(3)
    #
    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_five_mins_custom_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.five_mins_custom_test()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_custom_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.custom_test()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_trending_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.trending_test()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_full_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.full_test()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_chapter_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.chapter_test()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_search_module(self):
        self._login_with_password()
        SM = Search_Module(self.driver)
        SM.search_module_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_search_video(self):
        self._login_with_password()
        SM = Search_Module(self.driver)
        SM.search_learn_video_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_search_practice(self):
        self._login_with_password()
        SM = Search_Module(self.driver)
        SM.search_practice_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_search_questions(self):
        self._login_with_password()
        SM = Search_Module(self.driver)
        SM.search_question_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_search_books(self):
        self._login_with_password()
        SM = Search_Module(self.driver)
        SM.search_book_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_search_ptr(self):
        self._login_with_password()
        SM = Search_Module(self.driver)
        SM.search_PTR_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_search_test(self):
        self._login_with_password()
        SM = Search_Module(self.driver)
        SM.search_test_and_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_profile_menu(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_manage_profile()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_edit_goal_exam(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_edit_goal()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_edit_profile(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_edit_profile_name()


    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_profile_menu_settings(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_settings()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_profile_menu_change_language(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_change_lang()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_menu_tos(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_tos()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_menu_privacy_policy(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_privacy_policy()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_menu_help_center(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_help_center()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_menu_feedback(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_help_center()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_UH_module_click(self):
        self._login_with_password()
        UH = UserHome(self.driver)
        UH.UH_module_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_UH_add_fav_book_click(self):
        self._login_with_password()
        UH = UserHome(self.driver)
        UH.UH_add_fav_books()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_UH_test_i_have_taken(self):
        self._login_with_password()
        UH = UserHome(self.driver)
        UH.UH_Test_i_have_taken()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_UH_bookmark_videos(self):
        self._login_with_password()
        UH = UserHome(self.driver)
        UH.UH_bookmark_videos()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_UH_bookmark_questions(self):
        self._login_with_password()
        UH = UserHome(self.driver)
        UH.UH_bookmark_questions()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_UH_embibe_big_books(self):
        self._login_with_password()
        UH = UserHome(self.driver)
        UH.UH_embibe_big_books()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_menu_signout(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_sign_out()










