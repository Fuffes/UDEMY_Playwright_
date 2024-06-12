from playwright.sync_api import Page
import unittest
import pytest


@pytest.fixture(autouse=True)
def setUp(page: Page):
    my_page = page
    yield my_page
    print("gg")
   

def test_foobar(setUp):
    page = setUp
    page.goto("https://www.microsoft.com/pl-pl/")
    page.locator('//*[@id="card-body-highlight-uid17a8"]/div[3]/a').click()

    assert page.evaluate("1+1") == 2

