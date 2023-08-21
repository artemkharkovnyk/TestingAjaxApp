import pytest
from time import sleep
from framework.pages import LoginPage, RootPage, CurrentPage, LoggedInUserPage, MenuPage, SettingsPage
from framework.logger import tests_logger as logger


@pytest.fixture(autouse=True)
def user_login_fixture():
    """
    A fixture to handle user login.

    This fixture navigates to the login page from the root page.
    """
    expected_page = RootPage() 
    if expected_page.is_root_page():
        expected_page.go_to_login_page()
    else:
        raise
    


@pytest.fixture(autouse=True)
def user_data_fixture():
    """
    A fixture to provide user data for tests.

    Returns:
        dict: User data including email and password.
    """
    return {
        'email':'qa.ajax.app.automation@gmail.com',
        'password':'qa_automation_password'
    }

@pytest.fixture(autouse=True)
def return_to_root_page_fixture():
    """
    A fixture to return to the root page after each test.

    This fixture handles returning to the root page from the LoggedInUserPage
    or LoginPage depending on the current page context.
    """

    yield
    sleep(2)
    curent_page = CurrentPage().get()
    if curent_page == 'LoggedInUserPage':
        LoggedInUserPage().go_to_menu_page()
        MenuPage().go_to_settings()
        SettingsPage().logout()
    if curent_page == 'LoginPage':
        LoginPage().back()
    sleep(2)



    

        
    

