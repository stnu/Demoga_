from pages.base_page import BasePage

from components.component import WebElement


class RadiobPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/radio-button"
        self.btn_yes = WebElement(driver, locator="div:nth-child(2) > label")
        self.btn_Impressive = WebElement(driver, locator="div:nth-child(3) > label")
        self.btn_no = WebElement(driver, locator="div.custom-control.disabled.custom-radio.custom-control-inline")
        self.inf = WebElement(driver, locator="div:nth-child(2) > p > span")

        super().__init__(driver, self.base_url)
