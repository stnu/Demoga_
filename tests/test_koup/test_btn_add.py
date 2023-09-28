from pages.herokuapp_page import HerokuappPage
from pages.checkbox import CheckboxPage
from pages.herokuapp2_page import HerokuappPage2
from components.component import WebElement
import time


def test_find_elements(browser):
    demo_hero = HerokuappPage(browser)
    demo_hero2 = HerokuappPage2(browser)
    demo_hero.visit()
    assert demo_hero.link.get_text() == "Add/Remove Elements"
    demo_hero.link.click()
    assert demo_hero2.equal_url()
    time.sleep(3)

    assert demo_hero2.btn_add.get_text() == "Add Element"
    assert demo_hero2.btn_add.get_dom_attribute("onclick") == "addElement()"

    for i in range(4):  # кликаем 4 раза
        demo_hero2.btn_add.click()

    time.sleep(2)
    assert demo_hero2.btn_del.check_count_elements(count=4)

    for element in demo_hero2.btn_del.find_elements():  # проверим для всех элементов
        assert element.text == "Delete"

    assert demo_hero2.btn_del.get_text() == "Delete"  # проверяем только для первого элемента

    while demo_hero2.btn_del.exist():
        demo_hero2.btn_del.click()

    assert not demo_hero2.btn_del.exist()
    time.sleep(5)


    #all_btn_del = demo_hero2.btn_del.find_elements()

    #for button in all_btn_del:
        #button.click()
    #assert demo_hero2.btn_del.check_count_elements(count=0)