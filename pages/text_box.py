from pages.base_page import BasePage

from components.component import WebElement


class TextboxPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/text-box"
        self.user_n = WebElement(driver, locator="#userName")
        self.adress = WebElement(driver, locator='[placeholder="Current Address"]')
        self.user_n_as = WebElement(driver, locator="#name")
        self.adress_as = WebElement(driver, locator="p#currentAddress")
        self.btn_submit = WebElement(driver, locator="#submit")
        super().__init__(driver, self.base_url)
