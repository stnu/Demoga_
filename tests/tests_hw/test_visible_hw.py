from pages.accordion import AccordionPage
from pages.elements_page import ElementsPage
import time


def test_visible_accordion(browser):
    demo_accordion = AccordionPage(browser)
    demo_accordion.visit()
    assert demo_accordion.section1.visible()
    demo_accordion.what.click()
    time.sleep(2)
    assert not demo_accordion.section1.visible()


def test_visible_accordion_default(browser):
    demo_accordion = AccordionPage(browser)
    demo_accordion.visit()
    assert not demo_accordion.section2_ch1.visible()
    assert not demo_accordion.section2_ch2.visible()
    assert not demo_accordion.section3.visible()
