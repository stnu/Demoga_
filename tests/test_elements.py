from pages.elements_page import ElementsPage
from pages.checkbox import CheckboxPage


def test_find_elements(browser):
    demo_element = ElementsPage(browser)
    demo_element.visit()
    assert demo_element.btns_first_menu.check_count_elements(count=9)


def test_box(browser):
    demo_box = CheckboxPage(browser)
    demo_box.visit()
    assert demo_box.check_box.check_count_elements(count=1)
    demo_box.plus.click()
    assert demo_box.check_box.check_count_elements(count=17)
    demo_box.refresh()
    assert demo_box.check_box.check_count_elements(count=1)
