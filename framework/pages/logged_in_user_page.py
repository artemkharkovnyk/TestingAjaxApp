from time import sleep
from .page import Page
from .current_page import CurrentPage
from framework.logger import tests_logger as logger

class LoggedInUserPage(Page):
    """
    A class representing the logged-in user page in a mobile automation framework.
    Inherits from the Page class.
    """
    def is_logged_in_user_page(self) -> bool:
        """
        Check if the current page is the logged-in user page.

        Returns:
            bool: True if the page indicates a logged-in user, otherwise False.
        """
        possible_identificators = [
            'com.ajaxsystems:id/noHubs'
            # There should be an indicator in case the user has at least one hub.
        ]
        logger.info('Trying to find logged in user page elements')
        for identificator in possible_identificators:
            if self.find_element_by_id(identificator) is not None:
                return True
        return False
    
    @CurrentPage.page_change('MenuPage')
    def go_to_menu_page(self) -> None:
        """
        Navigate to the menu page.

        This method clicks the menu button.
        """
        self.click_element('com.ajaxsystems:id/menuDrawer')

    def wait_to_login(self) -> bool:
        """
        Wait for successful login.

        Returns:
            bool: True if the login is successful, False otherwise.
        """
        logger.info('Waiting 10 second to login')
        sleep(10)
        try:
            if self.is_logged_in_user_page():
                logger.info('Successful login')
                return True
            else:
                raise
        except Exception as e:
            logger.info(f'Failed to login. {e}')
            CurrentPage().set_page('LoginPage')
            return False







