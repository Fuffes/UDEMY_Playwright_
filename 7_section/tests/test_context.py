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
   
    context_2= browser.new_context()
    page_1 = context_1.new_page()
    page_2= context_2.new_page()

    page_1.goto("https://www.youtube.com/")
    page_2.goto("https://www.youtube.com/")
