from pages.base_page import BasePage

from components.component import WebElement


class CheckboxPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/checkbox"
        self.check_box = WebElement(driver, locator=".rct-icon.rct-icon-uncheck")
        self.plus = WebElement(driver, locator="#tree-node > div > button.rct-option.rct-option-expand-all > svg")
        super().__init__(driver, self.base_url)
