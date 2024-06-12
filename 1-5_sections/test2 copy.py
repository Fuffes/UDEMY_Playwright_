import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    context.tracing.start(snapshots=True,screenshots=True, sources=True )


    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("dddd")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("ddddd")
    page.locator("[data-test=\"login-button\"]").click()

    # ---------------------
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
