from pages.form_page import FormPage
from pages.webtables_page import WebtablesPage
import time

from selenium.webdriver.common.by import By


def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()
    assert form_page.first_name.get_dom_attribute("placeholder") == "First Name"
    assert form_page.last_name.get_dom_attribute("placeholder") == "Last Name"
    assert form_page.user_email.get_dom_attribute(
        "pattern") == "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
    form_page.bnt_submit.click_force()

    assert form_page.user_form.get_dom_attribute(
        "class") == "was-validated"


def test_add(browser):
    W_page = WebtablesPage(browser)
    W_page.visit()
    W_page.btn_add.click()
    W_page.first_name.send_keys("tester")
    W_page.last_name.send_keys("tester")
    W_page.user_email.send_keys("tester@mail.ru")
    W_page.user_age.send_keys("5")
    W_page.user_salary.send_keys("1")
    W_page.user_department.send_keys("tester")
    W_page.btn_submit.click_force()
    assert not W_page.reg_form.exist()


def test_webtables_next(browser):
    W_page = WebtablesPage(browser)
    W_page.visit()
    W_page.new_str(browser)
    W_page.new_str(browser)

    assert W_page.btn_next.get_dom_attribute("disabled") == "true"
    assert W_page.btn_prev.get_dom_attribute("disabled") == "true"
    W_page.new_str(browser)
    W_page.new_str(browser)
    W_page.new_str(browser)
    W_page.new_str(browser)
    W_page.new_str(browser)
    W_page.new_str(browser)
    W_page.new_str(browser)
    W_page.btn_next.click_force()
    W_page.driver.switch_to.window(W_page.driver.window_handles[0])
    assert W_page.input_number.get_dom_attribute("value") == "2"
    W_page.btn_prev.click_force()
    time.sleep(3)


