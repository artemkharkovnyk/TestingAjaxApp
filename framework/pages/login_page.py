from .page import Page
from .current_page import CurrentPage
from framework.logger import tests_logger as logger


class LoginPage(Page):
    """
    A class representing the login page in a mobile automation framework.
    Inherits from the Page class.
    """

    def _enter_email(self, email:str) -> None:
        """
        Enter the email in the email input field.

        Args:
            email (str): The email to enter.
        """
        self.enter('com.ajaxsystems:id/authLoginEmail', email)
        logger.info(f"Entered email: '{email}'")
        
    def _enter_password(self, password:str) -> None:
        """
        Enter the password in the password input field.

        Args:
            password (str): The password to enter.
        """
        self.enter('com.ajaxsystems:id/authLoginPassword', password)
        logger.info(f"Entered password: '{password}'")

    def _click_login(self) -> None:
        """
        Click the login button.
        """
        self.click_element('com.ajaxsystems:id/authLogin')
        logger.info(f"Login attempt")

    def is_login_page(self) -> bool:
        """
        Check if the current page is the login page.

        Returns:
            bool: True if the required identifiers are found, otherwise False.
        """
        required_identificators = [
            'com.ajaxsystems:id/authLoginPassword',
            'com.ajaxsystems:id/authLoginEmail'
        ]
        logger.info('Trying to find login page elements')
        return None not in list(map(self.find_element_by_id, required_identificators))
        
    @CurrentPage.page_change('LoggedInUserPage')
    def login(self, email:str, password:str) -> None:
        """
        Login with the provided email and password.

        Args:
            email (str): The email to use for login.
            password (str): The password to use for login.
        """
        self._enter_email(email)
        self._enter_password(password)
        self._click_login()
        

    @CurrentPage.page_change('RootPage')
    def back(self) -> None:
        """
        Go back to the previous page.

        This method simulates clicking the back button.
        """
        self.click_element('com.ajaxsystems:id/back')
        







