import re

import pytest
def verify_agent_url():
  value = "https://a.nel.cloudflare.com/report/v3?s=qga5uRSdy%2BogvYzJ7hfX9u78%2FBn2KkJpOkro0iNua0PX%2Bcm77dyKNGac2WNM8NMUN1q92mq2VnGACZAVZhk%2FWXzU1K1BPabZQIYGfbIuAyOxnO0UIBBmv%2Fm6X17Z2A%3D%3D"
  result = re.match('^https://a.nel.cloudflare.com/report/v3', value);

  print(result)
  print("....;;;;;")

