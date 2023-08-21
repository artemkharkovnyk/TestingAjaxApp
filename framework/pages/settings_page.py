from .page import Page
from .current_page import CurrentPage


class SettingsPage(Page):
    """
    A class representing the settings page in a mobile automation framework.
    Inherits from the Page class.
    """

    @CurrentPage.page_change('RootPage')
    def logout(self) -> None:
        """
        Perform logout action.

        This method clicks the logout button to log out the user.
        """
        self.click_element('com.ajaxsystems:id/accountInfoLogoutNavigate')

