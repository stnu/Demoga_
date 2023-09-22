from pages.elements_page import ElementsPage


def test_find_elements(browser):
    demo_element = ElementsPage(browser)
    demo_element.visit()
    assert demo_element.btns_first_menu.check_count_elements(count=9)
