import pytest
from playwright.sync_api import sync_playwright

with sync_playwright() as sync_p:
    browser = sync_p.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("https://www.youtube.com/")


    def test_login(page, browser_type):
        browser_type.launch(headless=False )
        page.goto("https://www.youtube.com/")

    # context.close()
    browser.close()