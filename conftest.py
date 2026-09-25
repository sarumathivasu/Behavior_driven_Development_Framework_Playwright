from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture
def page():
    playwright=sync_playwright().start()
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    yield page
    browser.close()
    playwright.stop()