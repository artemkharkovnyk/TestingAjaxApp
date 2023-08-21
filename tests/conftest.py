import pytest
from appium import webdriver
from framework.services import Appium
from framework.pages.current_page import CurrentPage

from utils.android_utils import android_get_desired_capabilities

appium_service = None


@pytest.fixture(scope='session')
def appium():
    """
    Appium fixture to manage the Appium server instance for the session.

    This fixture starts the Appium server once for the entire test session.

    Returns:
        Appium: An instance of the Appium service.
    """
    global appium_service
    if appium_service:
        return appium_service
    appium_service = Appium()
    return appium_service


@pytest.fixture(scope='session', autouse=True)
def setup(appium):
    """
    Setup fixture to start the Appium server and create the WebDriver instance.

    This fixture starts the Appium server, creates a WebDriver instance,
    and sets the current page using the WebDriver instance.

    Args:
        appium (Appium): The Appium service instance.
    """
    appium.start()
    driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub', desired_capabilities=android_get_desired_capabilities())
    CurrentPage(driver)

   
@pytest.fixture(scope='session', autouse=True)
def teardown(appium):
    """
    Teardown fixture to stop the Appium server at the end of the session.

    This fixture stops the Appium server once all tests in the session are done.

    Args:
        appium (Appium): The Appium service instance.
    """
    yield
    appium.stop()


