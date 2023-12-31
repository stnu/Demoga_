from pages.elements_page import ElementsPage


def test_flex_menu(browser):
    demo_element = ElementsPage(browser)
    demo_element.visit()
    assert demo_element.block_menu.check_css("flex", '0 0 25%')
    assert demo_element.block_menu.check_css("max-width", '25%')
    browser.set_window_size(400, 876)
    assert demo_element.block_menu.check_css("flex", '0 0 100%')
    assert demo_element.block_menu.check_css("max-width", '100%')
    browser.set_window_size(1000, 1000)