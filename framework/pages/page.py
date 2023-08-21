from appium.webdriver import Remote
from appium.webdriver.common.mobileby import MobileBy
from typing import Optional
from selenium.webdriver.remote.webelement import WebElement
from .current_page import CurrentPage
from framework.logger import tests_logger as logger

class Page:
    """
    A base class for page objects in a mobile automation framework.
    """
    def __init__(self, driver:Remote=None):
        """
        Initialize a Page object.

        Args:
            driver (Remote): An instance of the WebDriver.
        """
        if driver is None:
            self.driver:Remote = CurrentPage().get_driver()
        else:
            self.driver:Remote = driver

    def find_element_by_id(self, identifier:str) -> Optional[WebElement]:
        """
        Find an element on the page using its ID.

        Args:
            identifier (str): The ID of the element.

        Returns:
            WebElement: The found element or None if not found.
        """
        try:
            logger.info(f'Trying to find element with id {identifier}')
            element = self.driver.find_element(MobileBy.ID, identifier)
            return element
        except Exception as e:
            logger.info(f'Failed to find element with id {identifier}. {e}')
            return None

    def click_element(self, identifier:str) -> None:
        """
        Click an element on the page using its ID.

        Args:
            identifier (str): The ID of the element to click.
        """
        self.find_element_by_id(identifier).click()
        logger.info(f'Klicked on {identifier}')

    def enter(self, identifier:str, data:str) -> None:
        """
        Enter data into an input field on the page.

        Args:
            identifier (str): The ID of the block containing the input field.
            data (str): The data to enter into the input field.
        """
        block = self.find_element_by_id(identifier)
        field = block.find_element(MobileBy.CLASS_NAME, 'android.widget.EditText')
        field.send_keys(data)
        