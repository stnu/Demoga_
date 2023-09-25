from pages.base_page import BasePage

from components.component import WebElement


class ModalPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/modal-dialogs"
        self.menu = WebElement(driver, locator=".show > ul:nth-child(1) > li")
        self.icon = WebElement(driver, locator="#app > header > a > img")


        super().__init__(driver, self.base_url)
