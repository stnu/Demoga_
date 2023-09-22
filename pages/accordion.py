from pages.base_page import BasePage

from components.component import WebElement


class AccordionPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/accordian"
        self.section1 = WebElement(driver, locator="#section1Content > p")
        self.what = WebElement(driver, locator="#section1Heading")
        self.section2_ch1 = WebElement(driver, locator="#section2Content > p:nth-child(1)")
        self.section2_ch2 = WebElement(driver, locator="#section2Content > p:nth-child(2)")
        self.section3 = WebElement(driver, locator="#section3Content > p")
        super().__init__(driver, self.base_url)
