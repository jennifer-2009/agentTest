#!/usr/bin/python
# coding:utf-8

import requests
import json
import os
import re
import time



def sendDingAlert(info):
    # url = "https://oapi.dingtalk.com/robot/send?access_token=207fed619d52d5a69fc5e153780160fb226c7f6b22365873763576dcb22204c5"
    url = "https://oapi.dingtalk.com/robot/send?access_token=ee82fa2fac51d325645dd8c5b7f27b756f1cdd7ab58fc7d0b63463fb296b59c9"
    data = {"msgtype": "markdown", "markdown": {"title": "经纪人域名错误", "text": info}, }
    header = {"Content-Type": "application/json"}
    r = requests.post(url, data=json.dumps(data), headers=header)



def runCase(case):
    f = os.popen(" ".join(["pytest", "-s", case, "2>&1"]))
    logs = f.read()
    f.close()
    return logs


f = os.popen(" ".join(["ls", "house_agent/test_agent_domain_availability.py"]))
#f = os.popen(" ".join(["ls", "test_folder/test_CatchError.py"]))
apiCases = f.readlines()
f.close()
# print(apiCases)


for case in apiCases:
    logs = runCase(case.rstrip("\n"))
    print(logs)
    if 'FAILURE:' in logs or 'ERROR:' in logs:
        target = 'FAILURE:'
        bugs = []

        pattern1 = re.compile(target + ' \\d+', re.S)
        pattern2 = re.compile(target + ' ((?:https?:\/\/)?[^./]+(?:\.[^./]{2,3}))', re.S)
        result1 = pattern1.findall(logs)
        result2 = pattern2.findall(logs)

        if result1:
            bugs.extend(result1)
            #bugs.extend("\n")
        if result2:
            bugs.extend(result2)
        print(type(bugs))
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        info = "经纪人域名错误: "

        info = info + "\n" + '/'.join(bugs)
        info = "\n" + info + "\n" +t
        print(info)

        sendDingAlert(info)
