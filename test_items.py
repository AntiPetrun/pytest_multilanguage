import time

from selenium.webdriver.common.by import By


def test_button_add_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    # time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert button, 'Button doesn\'t exist'
    assert button.get_attribute('value') == button.text, 'Button attribute doesn\'t match value'
    button.click()
