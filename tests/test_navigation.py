from conftest import browser
from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage
from components.component import WebElement
import time


def test_navigation(browser):
    demo_p = Demoqa(browser)
    demo_element = ElementsPage(browser)
    demo_p.visit()
    demo_p.btn_elements.click()

    demo_p.refresh()
    browser.refresh()
    browser.back()
    browser.forward()

    demo_element.equal_url()



