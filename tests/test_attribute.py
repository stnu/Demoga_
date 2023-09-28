from pages.text_box import TextboxPage
import time


def test_placeholder(browser):
    text_page = TextboxPage(browser)
    text_page.visit()
    assert text_page.user_n.get_dom_attribute("placeholder") == "Full Name"
