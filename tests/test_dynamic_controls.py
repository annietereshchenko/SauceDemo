from pages.dynamic_controls_page import DynamicControlsPage


class TestDynamicControls:

    def test_remove_checkbox(self, browser):
        page = DynamicControlsPage(browser)
        page.open()
        page.remove_checkbox()
        assert page.is_element_present() == []

    def test_disabled_input(self, browser):
        page = DynamicControlsPage(browser)
        page.open()
        assert page.is_element_disabled() is True

    def test_enabled_input(self, browser):
        page = DynamicControlsPage(browser)
        page.open()
        page.click_on_button()
        assert page.is_element_disabled() is False
