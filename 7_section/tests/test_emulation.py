from playwright.sync_api import sync_playwright, Playwright


def run(playwright):
    # pixel_2 = playwright.devices["Pixel 2"]
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(
        # **pixel_2,
        # user_agent="Nata"
        viewport={"height": 1280, "width": 1024},
    )

    context2 = browser.new_context(
        viewport={"height": 500, "width": 500},
        device_scale_factor=2,
        locale="de-DE",
        timezone_id="Europe/Berlin",
    )

    page = context.new_page()
    page2 = context2.new_page()
    page.goto("https://youtube.com")
    page2.goto("https://youtube.com")
    page.pause()


with sync_playwright() as playwright:
    run(playwright)