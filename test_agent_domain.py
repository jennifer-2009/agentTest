import json
import re
import pytest
import requests
import selenium
PATH = 'driver/chromedriver'


def test_domain_avaliable():
 response = requests.get("http://api.51home.ca/api/agent?offset=0&limit=350&language=0&city=0&sort=0&order=desc")
 json_data = response.json()

 for data in json_data['data']:
     domain = data['public_domain']
     print(domain)
     r2 = requests.get(domain)
     r2_data = r2.headers
     report_to = r2_data.get('Report-To')
     json_report_to = json.loads(report_to)
     str_url = json_report_to['endpoints'][0]['url']
     print("report_to: ", str_url)
     assert re.match('^https://a.nel.cloudflare.com/report/v3', str_url)