import json
import re
import pytest
import pytest_check as check
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

PATH = 'driver/chromedriver'


def test_agent_domain_availabilities():
    options = webdriver.ChromeOptions()
    options.headless = True
    response = requests.get("http://api.51home.ca/api/agent?offset=0&limit=500&language=0&city=0&sort=0&order=desc")
    json_data = response.json()

    for data in json_data['data']:
        realtor_id = data['realtor_id']
        domain = data['public_domain']
        print(realtor_id)
        print(domain)
        driver = webdriver.Chrome(PATH, options=options)
        try:
            driver.get(domain)
        except WebDriverException:
            print(domain)
            check.is_false("Check if there is a typo in url --- ", realtor_id)
            check.is_false(domain)
        try:
            driver.find_element_by_css_selector('#masthead[role="banner"]')
        except NoSuchElementException:
            print(domain)
            check.is_false('No expected banner on the web page --- #masthead[role="banner"]', realtor_id)
            check.is_false(domain)
        try:
            driver.find_element_by_css_selector('.agent-avator img[src*="51agents"]')
        except NoSuchElementException:
            print(domain)
            check.is_false('No agent img on the footer of the web page --- .agent-avator img[src*="51agents"]', realtor_id)
            check.is_false(domain)
        driver.quit()
