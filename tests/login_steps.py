from pytest_bdd import given, when, then, parsers
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@given("the user navigates to the login page")
def user_navigates_to_login_page(page: Page):

    login_page = LoginPage(page)

    login_page.navigate(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )


@when(
    parsers.parse(
        'the user enters "{username}" and "{password}"'
    )
)
def user_enters_credentials(page: Page, username, password):

    login_page = LoginPage(page)

    login_page.login(username, password)


@then(
    parsers.parse(
        'the "{expected_result}" should be displayed'
    )
)
def verify_login_result(page: Page, expected_result):

    if expected_result == "Dashboard":

        expect(page).to_have_url(
            "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index",
            timeout=15000
        )

        expect(
            page.get_by_role("heading", name="Dashboard")
        ).to_be_visible()

    elif expected_result == "Invalid credentials":

        expect(
            page.get_by_text("Invalid credentials")
        ).to_be_visible()