from pages.base_page import BasePage

from components.component import WebElement


class AlertPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/alerts"
        self.btn_al = WebElement(driver, locator="#alertButton")
        self.btn_al_2 = WebElement(driver, locator="#confirmButton")
        self.btn_al_3 = WebElement(driver, locator="#promtButton")
        self.comf_res = WebElement(driver, locator="#confirmResult")
        self.promt_res = WebElement(driver, locator="#promptResult")
        self.btn_al_time = WebElement(driver, locator="#timerAlertButton")

        super().__init__(driver, self.base_url)