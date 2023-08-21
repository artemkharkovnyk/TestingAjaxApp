from framework.pages import LoggedInUserPage, LoginPage
from framework.logger import tests_logger as logger


def test_user_login(user_login_fixture, user_data_fixture, return_to_root_page_fixture):
    """
    Test user login with valid credentials.

    This test case covers the successful user login scenario using valid credentials.

    Args:
        user_login_fixture: fixture to initiate the login process.
        user_data_fixture (dict): User data containing email and password.
        return_to_root_page_fixture: Fixture to ensure returning to the root page after the test.

    Steps:
    1. Ensure that the login page is displayed.
    2. Extract user email and password from the user_data_fixture.
    3. Perform login using extracted credentials.
    4. Check if the user is successfully logged in by waiting for the logged in user page.

    Expected Result:
    - The user should be successfully logged in.
    - The LoggedInUserPage should be displayed.

    """
    logger.info(' -- TEST test_user_login -- ')
    login_page = LoginPage()
    assert login_page.is_login_page()
    email:str = user_data_fixture['email']
    password:str = user_data_fixture['password']
    login_page.login(email, password)
    logged_in_user_page = LoggedInUserPage()
    assert logged_in_user_page.wait_to_login()
    


def test_user_login_with_wrong_password(user_login_fixture, user_data_fixture, return_to_root_page_fixture):
    """
    Test user login with wrong password.

    This test case covers the scenario where the user attempts to login with a wrong password.

    Args:
        user_login_fixture (LoginPage): LoginPage fixture to initiate the login process.
        user_data_fixture (dict): User data containing email and password.
        return_to_root_page_fixture: Fixture to ensure returning to the root page after the test.

    Steps:
    1. Ensure that the login page is displayed.
    2. Extract user email from the user_data_fixture.
    3. Perform login using the extracted email and a wrong password.
    4. Check that the user is not successfully logged in.
    5. Check that the login page is displayed again.

    Expected Result:
    - The user should not be able to log in.
    - The login page should be displayed again.

    """
    logger.info(' -- TEST test_user_login_with_wrong_password -- ')
    login_page = LoginPage()
    assert login_page.is_login_page()
    email:str = user_data_fixture['email']
    worng_password:str = '12345'
    login_page.login(email, worng_password)
    assert not LoggedInUserPage().wait_to_login()
    assert login_page.is_login_page()
    

def test_user_login_with_wrong_email(user_login_fixture, user_data_fixture, return_to_root_page_fixture):
    """
    Test user login with wrong email.

    This test case covers the scenario where the user attempts to login with a wrong email.

    Args:
        user_login_fixture (LoginPage): LoginPage fixture to initiate the login process.
        user_data_fixture (dict): User data containing email and password.
        return_to_root_page_fixture: Fixture to ensure returning to the root page after the test.

    Steps:
    1. Ensure that the login page is displayed.
    2. Extract user password from the user_data_fixture.
    3. Perform login using a wrong email and the extracted password.
    4. Check that the user is not successfully logged in.
    5. Check that the login page is displayed again.

    Expected Result:
    - The user should not be able to log in.
    - The login page should be displayed again.

    """
    logger.info(' -- TEST test_user_login_with_wrong_email -- ')
    login_page = LoginPage()
    assert login_page.is_login_page()
    wrong_email:str = 'wrong@gmail.com'
    password:str = user_data_fixture['password']
    login_page.login(wrong_email, password)
    assert not LoggedInUserPage().wait_to_login()
    assert login_page.is_login_page()

