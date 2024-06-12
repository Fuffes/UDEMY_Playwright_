# def test_page(page):
#     page.goto("https://www.microsoft.com/ru-by")
#     page.locator('//*[@id="card-body-highlight-uid26e7"]/div[3]/a').click()


from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    iphone_11 = p.devices["iPhone 11 Pro"]
    browser = p.webkit.launch(headless=False, slow_mo=5000)
    context_1 = browser.new_context(
        **iphone_11,
        locale="de-DE", 
        geolocation={"longitude": 12.492507, "latitude": 41.889938}, 
        permissions=["geolocation"]
    )
   
    page_1 = context_1.new_page()
    page_1.goto("https://www.youtube.com/")
    page_1.pause()
    page_1.goto("https://www.youtube.com/watch?v=ys_lnAlof04")
    browser.close()