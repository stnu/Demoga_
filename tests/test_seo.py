import pytest

from conftest import browser
from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage
from components.component import WebElement
from pages.accordion import AccordionPage
from pages.alert_page import AlertPage
from pages.browser_page import BrowserTab

import time


def test_seo(browser):
    demo_page = Demoqa(browser)
    demo_page.visit()
    assert browser.title == "DEMOQA"


@pytest.mark.parametrize("pages", [AccordionPage, AlertPage, Demoqa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == "DEMOQA"
    