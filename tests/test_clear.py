from pages.text_box import TextboxPage
import time


def test_clear(browser):
    text_page = TextboxPage(browser)
    text_page.visit()
    text_page.user_n.send_keys("tester")
    time.sleep(2)
    text_page.user_n.clear()
    time.sleep(2)
    assert text_page.user_n.get_text() == ""
