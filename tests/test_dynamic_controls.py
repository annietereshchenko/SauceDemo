from pages.dynamic_controls_page import DynamicControlsPage


class TestDynamicControls:

    def test_remove_checkbox(self, browse_dc):
        page = DynamicControlsPage(browse_dc)
        page.remove_checkbox()
        assert page.is_checkbox_present() == 0

    def test_disabled_input(self, browse_dc):
        page = DynamicControlsPage(browse_dc)
        assert page.is_element_disabled() is True

    def test_enabled_input(self, browse_dc):
        page = DynamicControlsPage(browse_dc)
        page.click_on_enable_button()
        assert page.is_element_disabled() is False
