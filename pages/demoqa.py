from pages.base_page import BasePage

from components.component import WebElement


class Demoqa(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/"
        self.icon = WebElement(driver, locator="#app>header>a")
        self.btn_elements = WebElement(driver, locator="#app>div>div>div.home-body>div>div:nth-child(1)")
        self.footer = WebElement(driver, locator="footer > span")
        super().__init__(driver, self.base_url)

