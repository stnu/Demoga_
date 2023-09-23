from pages.form_page import FormPage
import time

from selenium.webdriver.common.by import By

def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys("tester")
    form_page.last_name.send_keys("testeravich")
    form_page.user_name.send_keys("test@ttt.tt")
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys("9992223344")
    form_page.bnt_hobbies.click_force()
    form_page.adress.send_keys("LA")
    time.sleep(2)
    form_page.bnt_submit.click_force()
    time.sleep(2)
    assert form_page.modal_dialog.exist()
    form_page.bnt_close_modal.click_force()


def test(browser):
    form_page = FormPage(browser)
    form_page.visit()
    form_page.scrol.click()
    time.sleep(2)
    form_page.scrol_1.click_force() # можно поставить scrol_0 и scrol_2

    time.sleep(2)
