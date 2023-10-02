import time

from pages.elements_page import ElementsPage
from pages.droppable import DroppablePage
from selenium.webdriver import ActionChains


def test_drag_and_drop(browser):
    demo_drop = DroppablePage(browser)

    action_chains = ActionChains(browser)
    demo_drop.visit()
    assert demo_drop.drop.check_css("backgroundColor", "rgba(0, 0, 0, 0)")

    action_chains.drag_and_drop(demo_drop.drag.find_element(), demo_drop.drop.find_element()).perform()
    time.sleep(2)

    assert demo_drop.drop.check_css("backgroundColor", "rgba(70, 130, 180, 1)")
    #assert demo_drop.drop.getCssValue("background-color") == '70, 130, 180, 1'
    action_chains.drag_and_drop_by_offset(demo_drop.drag.find_element(), -200, 0).perform()
    time.sleep(2)
    assert demo_drop.drop.check_css("backgroundColor", "rgba(70, 130, 180, 1)")
