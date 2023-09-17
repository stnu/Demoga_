from conftest import browser
from pages.demoqa import Demoqa


def test_icon_exist(browser):
    demo_page = Demoqa(browser)
    demo_page.visit()
    demo_page.icon.click()

    assert demo_page.equal_url()
    assert demo_page.icon.exist()
    # browser.get("https://demoqa.com/")

    # try:
    # browser.find_element(By.CSS_SELECTOR, "#app>header>a")
    # except NoSuchElementException:
    # assert False
    # assert True
