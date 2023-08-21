from appium.webdriver.webdriver import WebDriver

from framework.logger import tests_logger as logger


class CurrentPage:
    """
    Class to manage the current page state in a mobile automation framework.
    """

    __page = None
    __instance = None
    __driver = None

    def __new__(cls, driver:WebDriver=None) -> 'CurrentPage':
        """
        Create or reuse an instance of the CurrentPage class.

        Args:
            driver (WebDriver): An instance of the WebDriver.

        Returns:
            CurrentPage: An instance of the CurrentPage class.
        """
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__page = 'RootPage'
            if cls.__driver is None:
                cls.__driver = driver
        return cls.__instance
    
    def get_driver(self) -> WebDriver:
        """
        Get the WebDriver instance associated with the CurrentPage.

        Returns:
            WebDriver: The WebDriver instance.
        """
        return self.__driver
    
    def set_page(self, page:str) -> None:
        """
        Set the current page's name.

        Args:
            page (str): The name of the new current page.
        """
        logger.info(f'Page changed {self.__page} -> {page}')
        self.__page = page

    def get(self) -> str:
        """
        Get the name of the current page.

        Returns:
            str: The name of the current page.
        """
        return self.__page
    
    def page_change(page:str):
        """
        Decorator function to change the current page after executing a page-changing function.

        Args:
            page (str): The name of the page to set after the function is executed.

        Returns:
            function: A decorator that changes the page after executing a function.
        """
        def decorator(go_to_func: callable) -> callable:
            def execute_func_and_remember_page(*args, **kwargs):
                res = go_to_func(*args, **kwargs) 
                CurrentPage().set_page(page)
                return res
            return execute_func_and_remember_page
        return decorator

        
    
