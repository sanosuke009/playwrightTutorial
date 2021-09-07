import os
import time

from playwright.sync_api import Playwright, sync_playwright
import pytest

try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    import config
    PASSWORD = config.PASSWORD


@pytest.mark.smoke
@pytest.mark.regression
def test_login(playwright: Playwright) -> None:
    # Assess - Given
    browser = playwright.chromium.launch()
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    # Act - When/And
    # page.click("button:has-text('Log In')", timeout=2000)
    time.sleep(0.5)
    page.click("text=Log In", timeout=2000)
    # page.click("'Log In'", timeout=2000)
    page.click("[data-testid='signUp.switchToSignUp']")
    # page.click(":nth-match(:text('Log In'), 2)", timeout=2000)
    page.click("[data-testid='switchToEmailLink'] >> [data-testid='buttonElement']")
    # page.click("[data-testid='siteMembers.container'] input[type='email']")
    # page.fill("[data-testid='siteMembers.container'] input[type='email']", "symon.storozhenko@gmail.com")
    page.fill('input:below(:text("Email"))', "symon.storozhenko@gmail.com")
    page.press("[data-testid='siteMembers.container'] >> input[type='email']", "Tab")
    page.fill("input[type='password']", PASSWORD)
    page.click("[data-testid='submit'] >> [data-testid='buttonElement']")
    page.click("[aria-label='symon.storozhenko account menu']")

    # Assert - Then
    assert page.is_visible("text=My Orders")


    # ---------------------
    context.close()
    browser.close()


