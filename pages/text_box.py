from pages.base_page import BasePage

from components.component import WebElement


class TextboxPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/text-box"
        self.user_n = WebElement(driver, locator="#userName")

        super().__init__(driver, self.base_url)
