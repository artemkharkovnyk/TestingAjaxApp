from .page import Page
from .current_page import CurrentPage

class MenuPage(Page):
    """
    A class representing the menu page in a mobile automation framework.
    Inherits from the Page class.
    """
    @CurrentPage.page_change('SettingsPage')
    def go_to_settings(self) -> None:
        """
        Navigate to the settings page.

        This method clicks the application settings button.
        """
        self.click_element('com.ajaxsystems:id/settings')

