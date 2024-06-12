import asyncio

from playwright.async_api import async_playwright


from playwright.sync_api import sync_playwright


# with sync_playwright() as p:
#     browser = p.chromium.launch(headless = False, slow_mo = 500)
#     page = browser.new_page()
#     page.goto("https://www.saucedemo.com/")

#     browser.close()


async def main():
    async with async_playwright() as ap:
        browser = await ap.chromium.launch(headless=False, slow_mo = 2000)
        page = await browser.new_page()
        await page.goto("https://www.saucedemo.com/")
        await browser.close()

asyncio.run(main())

