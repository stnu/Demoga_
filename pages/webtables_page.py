from pages.base_page import BasePage

from components.component import WebElement


class WebtablesPage(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"
        self.btn_add = WebElement(driver, locator="#addNewRecordButton")
        self.first_name = WebElement(driver, locator="#firstName")
        self.last_name = WebElement(driver, locator="#lastName")
        self.user_email = WebElement(driver, locator="#userEmail")
        self.user_age = WebElement(driver, locator="#age")
        self.user_salary = WebElement(driver, locator="#salary")
        self.user_department = WebElement(driver, locator="#department")
        self.btn_submit = WebElement(driver, locator="#submit")
        self.reg_form = WebElement(driver, locator="body > div.fade.modal.show > div > div")
        self.no_rows = WebElement(driver, locator="div.rt-noData")
        self.btn_del = WebElement(driver, locator="[title = 'Delete']")
        self.str = WebElement(driver,
                              locator="#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(1)")
        self.btn_next = WebElement(driver, locator="div.-next > button")
        self.btn_prev = WebElement(driver, locator="div.-previous > button")

        self.input_number = WebElement(driver, locator="input[type = number]")


        super().__init__(driver, self.base_url)

    def new_str(self, browser):
        W_page = WebtablesPage(browser)
        W_page.btn_add.click()
        W_page.first_name.send_keys("tester")
        W_page.last_name.send_keys("tester")
        W_page.user_email.send_keys("tester@mail.ru")
        W_page.user_age.send_keys("5")
        W_page.user_salary.send_keys("1")
        W_page.user_department.send_keys("tester")
        W_page.btn_submit.click_force()
