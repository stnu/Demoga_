from pages.text_box import TextboxPage
import time


def test_clear(browser):
    text_page = TextboxPage(browser)
    text_page.visit()

    text_page.user_n.send_keys("tester")
    time.sleep(2)
    text_page.adress.send_keys("tester")
    time.sleep(2)
    text_page.btn_submit.click()
    assert text_page.user_n_as.get_text() == "Name:tester"
    assert text_page.adress_as.get_text() == "Current Address :tester"