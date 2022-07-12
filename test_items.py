import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_be_add_to_cart_btn(browser):
    browser.get(link)

    browser.implicitly_wait(10)
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert buttons, "There is no Add To Basket button"


