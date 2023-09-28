from pages.browser_page import BrowserTab
import time


def test_browser_tab(browser):
    browser_page = BrowserTab(browser)
    browser_page.visit()

    assert len(browser_page.driver.window_handles) == 1
    time.sleep(2)
    browser_page.new_tab.click()
    assert len(browser_page.driver.window_handles) == 2
    browser_page.driver.switch_to.window(browser_page.driver.window_handles[0])

    time.sleep(2)