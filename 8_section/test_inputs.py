from playwright.sync_api import Page


def test_facebook(page: Page):
    page.goto("https://www.facebook.com/register")
  
    page.locator('//*[@name="firstname"]').click()
    page.locator('//*[@name="firstname"]').fill("Dory")

    page.locator('//*[@name="lastname"]').click()
    page.locator('//*[@name="lastname"]').fill("Fish")


    page.locator('//*[@name="sex"]').nth(1).click()


