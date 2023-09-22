from pages.modal_dialogs import ModalPage


def test_modal_elements(browser):
    demo_modal = ModalPage(browser)
    demo_modal.visit()
    assert demo_modal.menu.check_count_elements(count=5)
