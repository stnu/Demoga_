from pages.base_page import BasePage

from components.component import WebElement


class FormPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/automation-practice-form"
        self.first_name = WebElement(driver, locator="#firstName")
        self.last_name = WebElement(driver, locator="#lastName")
        self.user_name = WebElement(driver, locator="#userEmail")
        self.gender_radio_1 = WebElement(driver, locator="#gender-radio-1")
        self.user_number = WebElement(driver, locator="#userNumber")
        self.bnt_submit = WebElement(driver, locator="#submit")
        self.modal_dialog = WebElement(driver, locator="body > div.fade.modal.show > div")
        self.bnt_close_modal = WebElement(driver, locator="#closeLargeModal")
        self.bnt_hobbies = WebElement(driver, locator="#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label")
        self.adress = WebElement(driver, locator="#currentAddress")
        self.scrol = WebElement(driver, locator="#state > div > div.css-1hwfws3>div")
        self.scrol_0 = WebElement(driver, locator="#react-select-3-option-0")
        self.scrol_1 = WebElement(driver, locator="#react-select-3-option-1")
        self.scrol_2 = WebElement(driver, locator="#react-select-3-option-2")

        super().__init__(driver, self.base_url)
