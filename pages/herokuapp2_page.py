from pages.base_page import BasePage

from components.component import WebElement


class HerokuappPage2(BasePage):

    def __init__(self, driver):
        self.base_url = "http://the-internet.herokuapp.com/add_remove_elements/"

        self.btn_add = WebElement(driver, locator="#content > div > button")
        self.btn_del = WebElement(driver, locator="[onclick = 'deleteElement()']")

        super().__init__(driver, self.base_url)


