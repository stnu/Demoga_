from pages.base_page import BasePage

from components.component import WebElement


class DroppablePage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/droppable"
        self.drag = WebElement(driver, locator="#draggable")
        self.drop = WebElement(driver, locator="#droppable")
        super().__init__(driver, self.base_url)
