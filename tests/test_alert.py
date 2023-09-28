from pages.alert_page import AlertPage
import time


def test_alert(browser):
    alert_page = AlertPage(browser)
    alert_page.visit()
    assert not alert_page.alert()
    alert_page.btn_al.click()
    time.sleep(2)
    assert alert_page.alert()
    alert_page.alert().accept()


def test_alert_text(browser):
    alert_page = AlertPage(browser)
    alert_page.visit()

    alert_page.btn_al.click()
    time.sleep(2)
    assert alert_page.alert().text == "You clicked a button"
    alert_page.alert().accept()
    assert not alert_page.alert()


def test_alert_confirm(browser):
    alert_page = AlertPage(browser)
    alert_page.visit()

    alert_page.btn_al_2.click()
    time.sleep(2)
    alert_page.alert().dismiss()
    assert alert_page.comf_res.get_text() == "You selected Cancel"


def test_alert_prompt(browser):
    alert_page = AlertPage(browser)
    alert_page.visit()

    alert_page.btn_al_3.click()
    time.sleep(2)
    alert_page.alert().send_keys("Аня")
    alert_page.alert().accept()
    time.sleep(2)
    assert alert_page.promt_res.get_text() == "You entered Аня"


def test_alert_time(browser):
    alert_page = AlertPage(browser)
    alert_page.visit()

    alert_page.btn_al_time.exist()
    alert_page.btn_al_time.click()

    time.sleep(5)

    assert alert_page.alert()
