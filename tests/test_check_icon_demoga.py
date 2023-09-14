from conftest import browser
from pages.demoqa import Demoqa


def test_icon_exist(browser):
    demo_page = Demoqa(browser)
    demo_page.visit()
    demo_page.click_on_the_icon()

    assert demo_page.equal_url()
    assert demo_page.exist_icon()
    # browser.get("https://demoqa.com/")

    # try:
    # browser.find_element(By.CSS_SELECTOR, "#app>header>a")
    # except NoSuchElementException:
    # assert False
    # assert True
