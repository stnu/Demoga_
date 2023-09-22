from conftest import browser

from pages.elements_page import ElementsPage

import time


def test_visible_btn_sidebar(browser):
    demo_p = ElementsPage(browser)
    demo_p.visit()
    # demo_p.sidebar_first_texbox.click()
    #time.sleep(3)
    # assert demo_p.btn_sidebar_first_texbox.exist()
    assert demo_p.btn_sidebar_first_texbox.visible()


def test_not_visible_bnt_siderbar(browser):
    demo_p = ElementsPage(browser)
    demo_p.visit()
    assert demo_p.btn_sidebar_first_checkbox.visible()
    demo_p.btn_sidebar_first.visible()
    demo_p.sidebar_first_texbox.click()
    time.sleep(2)
    assert not demo_p.btn_sidebar_first_checkbox.visible()

