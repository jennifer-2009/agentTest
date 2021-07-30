import pytest_check as check
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

PATH = 'driver/chromedriver'
from webdriver_manager.chrome import ChromeDriverManager


def test_error_domin():
    options = webdriver.ChromeOptions()
    options.headless = True
    # driver = webdriver.Chrome(PATH, options=options)

    #domain = "https://teamTronto.ca"
    domain = "https://jessicadreamhome.com"

    realtor_id = 12345
    id = 890

    isPass = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    try:
        driver.get(domain)
    except WebDriverException:
        isPass = False
        check.is_false("This site can’t be reached --- ", realtor_id)
        check.is_false("....", domain)
    if isPass:
        try:
            driver.find_element_by_css_selector('#masthead[role="banner"]')
        except NoSuchElementException:
            isPass = False
            check.is_false('No expected banner on the web page --- #masthead[role="banner"]', id)
            check.is_false("....", domain)
    if isPass:
        try:
            driver.find_element_by_css_selector('.agent-avator img[src*="51agents"]')
        except NoSuchElementException:
            print(domain)
            check.is_false('No agent img on the footer of the web page --- .agent-avator img[src*="51agents"]', id)
            check.is_false("....", domain)
    driver.quit()




test_error_domin()