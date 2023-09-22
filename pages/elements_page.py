from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from pages.demoqa import Demoqa
from components.component import WebElement


class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/elements"
        self.test_elem = WebElement(driver, locator="#app > div > div > div.pattern-backgound.playgound-header > div")
        self.select = WebElement(driver, locator="#app > div > div > div.row > div.col-12.mt-4.col-md-6")
        self.btn_sidebar_first = WebElement(driver, locator="div:nth-child(1) > span > div")
        self.btn_sidebar_first_texbox = WebElement(driver, locator="#item-0 > span")
        self.sidebar_first_texbox = WebElement(driver,
                                               locator="#app > div > div > div.row > div:nth-child(1) > div > div > div:nth-child(1) > span > div")
        self.btn_sidebar_first_checkbox = WebElement(driver,
                                                     locator="div:nth-child(1) > div > ul > #item-1> span")
        self.btns_first_menu = WebElement(driver,
                                          locator="div:nth-child(1) > div > ul > li")
        super().__init__(driver, self.base_url)
