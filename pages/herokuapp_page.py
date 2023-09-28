from pages.base_page import BasePage

from components.component import WebElement


class HerokuappPage(BasePage):

    def __init__(self, driver):
        self.base_url = "http://the-internet.herokuapp.com/"
        self.link = WebElement(driver, locator="#content > ul > li:nth-child(2) > a")



        super().__init__(driver, self.base_url)