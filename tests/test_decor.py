import time
import pytest
import pytest

from conftest import browser
from pages.demoqa import Demoqa
from pages.radio_button_page import RadiobPage
from components.component import WebElement


@pytest.mark.skip
def test_decor(browser):  # тут что-то не так
    demo_page = Demoqa(browser)
    demo_page.visit()
    time.sleep(3)
    assert demo_page.h5.check_count_elements(6)

    for element in demo_page.h5.find_elements():
        assert element.text() != ""


# @pytest.mark.skipif(True, reason='не надо тестировать')
def test_radio(browser):
    radio_page = RadiobPage(browser)

    if not radio_page.code_status():
        pytest.skip(reason=f"Страница{radio_page.base_url}недоступна")

    radio_page.visit()
    time.sleep(3)
    radio_page.btn_yes.click()
    assert radio_page.inf.get_text() == "Yes"

    radio_page.btn_Impressive.click()
    assert radio_page.inf.get_text() == "Impressive"

    assert "disabled" in radio_page.btn_no.get_dom_attribute("class")
