from playwright.sync_api import Page


def test_frames(page : Page):

    page.goto("https://developer.mozilla.org/en-US/docs/web/html/element/iframe")
    (page.frame_locator("iframe[title=\"MDN Web Docs Interactive Example\"]").get_by_text("</iframe>", exact=True).click())
    (page.frame_locator("iframe[title=\"MDN Web Docs Interactive Example\"]").get_by_role("textbox").fill(
        "<iframe\n  id=\"inlineFrameExample\"\n  title=\"Inline Frame Example\"\n  width=\"300\"\n  height=\"200\"\n  src=\"https://www.openstreetmap.org/export/embed.html?bbox=-0.004017949104309083%2C51.47612752641776%2C0.00030577182769775396%2C51.478569861898606&layer=mapnik\">\n</iframe>python\n\n"))

