from pages.demoqa import Demoqa
import time

def test_size(browser):
    demo_p = Demoqa(browser)
    demo_p.visit()
    browser.set_window_size(1000,300)
    time.sleep(2)
    browser.set_window_size(1000,1000)