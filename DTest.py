import requests
import json
import os
import re
import time


def sendDingAlert(info):
    # url = "https://oapi.dingtalk.com/robot/send?access_token=207fed619d52d5a69fc5e153780160fb226c7f6b22365873763576dcb22204c5"
    url = "https://oapi.dingtalk.com/robot/send?access_token=ee82fa2fac51d325645dd8c5b7f27b756f1cdd7ab58fc7d0b63463fb296b59c9"
    data = {"msgtype": "markdown", "markdown": {"title": "Agent Domain ERROR", "text": info}, }
    header = {"Content-Type": "application/json"}
    r = requests.post(url, data=json.dumps(data), headers=header)
    print(r)


def runCase(case):
    f = os.popen(" ".join(["pytest", "-s", case, "2>&1"]))
    logs = f.read()
    f.close()
    return logs

f = os.popen(" ".join(["ls", "/Users/jenniferjiang/QA/pythonProject/agentTest/house_agent/test_agent_domain_availability.py"]))
#f = os.popen(" ".join(["ls", "/Users/jenniferjiang/QA/pythonProject/agentTest/test_folder/test_CatchError.py"]))
apiCases = f.readlines()
f.close()
# print(apiCases)


for case in apiCases:
    logs = runCase(case.rstrip("\n"))
    print(logs)
    if 'FAILURE:' in logs or 'ERROR:' in logs:
        target = 'FAILURE:'
        bugs = []

        pattern1 = re.compile(target+' \\d+', re.S)
        result1 = pattern1.findall(logs)

        if result1:
            bugs.extend(result1)

        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        info = "#### Agent realtor_id: " + '/'.join(bugs)

        info = info + " ######\n" + t
        print(info)

sendDingAlert(info)
