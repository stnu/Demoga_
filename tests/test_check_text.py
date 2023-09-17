from conftest import browser
from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage
from components.component import WebElement


def test_page_elements(browser):
    demo_element = ElementsPage(browser)
    demo_element.visit()
    assert demo_element.test_elem.get_text() == "Elements"


def test_page_elements_footer(browser):
    demo_p = Demoqa(browser)
    demo_p.visit()
    assert demo_p.footer.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."


def test_page_elements_select(browser):
    demo_p = Demoqa(browser)
    demo_p.visit()
    demo_p.btn_elements.click()
    demo_element = ElementsPage(browser) # вот эта строчка мне не нравится, но я не придумала как рещить без нее
    assert demo_element.select.get_text() == "Please select an item from left to start practice."
