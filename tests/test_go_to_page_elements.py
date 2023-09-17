from conftest import browser
from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage



def test_go_to_page_elements(browser):
    demo_page = Demoqa(browser)
    demo_element = ElementsPage(browser)
    demo_page.visit()
    assert demo_page.equal_url()
    demo_page.btn_elements.click()
    assert demo_element.equal_url()
