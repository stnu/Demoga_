from pages.demoqa import Demoqa
import time
from pages.elements_page import ElementsPage


def test_size(browser):
    demo_p = Demoqa(browser)
    demo_p.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)


def test_visible_nav_bar(browser):
    demo_p = ElementsPage(browser)
    demo_p.visit()
    assert not demo_p.nav.visible()
    browser.set_window_size(400, 876)
    assert demo_p.nav.visible()
    browser.set_window_size(1000, 1000)

