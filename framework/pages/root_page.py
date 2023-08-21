from .page import Page
from .current_page import CurrentPage
from framework.logger import tests_logger as logger


class RootPage(Page):
    """
    A class representing the root page in a mobile automation framework.
    Inherits from the Page class.
    """
    def is_root_page(self) -> bool:
        """
        Check if the current page is the root page.

        Returns:
            bool: True if the root element is found, otherwise False.
        """
        logger.info('Trying for find root page eleent')
        return self.find_element_by_id('com.ajaxsystems:id/root') is not None
    
    @CurrentPage.page_change('LoginPage')
    def go_to_login_page(self) -> None:
        """
        Navigate to the login page.

        This method clicks the login button.
        """
        self.click_element('com.ajaxsystems:id/authHelloLogin')

