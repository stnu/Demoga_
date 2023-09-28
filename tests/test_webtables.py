from pages.form_page import FormPage
from pages.webtables_page import WebtablesPage
import time

from selenium.webdriver.common.by import By


def test_webtables(browser):
    W_page = WebtablesPage(browser)
    W_page.visit()

    assert not W_page.no_rows.exist()

    while W_page.btn_del.exist():
        W_page.btn_del.click()

    time.sleep(3)
    assert W_page.no_rows.exist()



