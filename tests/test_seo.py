from conftest import browser
from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage
from components.component import WebElement
import time


def test_seo(browser):
    demo_page = Demoqa(browser)
    demo_page.visit()
    assert browser.title == "DEMOQA"
