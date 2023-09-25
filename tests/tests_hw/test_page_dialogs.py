from pages.modal_dialogs import ModalPage
from pages.demoqa import Demoqa


def test_modal_elements(browser):
    demo_modal = ModalPage(browser)
    demo_modal.visit()
    assert demo_modal.menu.check_count_elements(count=5)


def test_navigation_modal(browser):
    demo_modal = ModalPage(browser)
    demo_page = Demoqa(browser)
    demo_modal.visit()
    browser.refresh()
    demo_modal.icon.click()
    demo_page.back()
    browser.set_window_size(900, 400)
    demo_modal.forward()
    assert demo_page.equal_url()
    assert browser.title == "DEMOQA"
    browser.set_window_size(1000, 1000)
