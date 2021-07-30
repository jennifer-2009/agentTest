import os
import time
import re
import requests
import json


def sendDingAlert(info):
    # url = "https://oapi.dingtalk.com/robot/send?access_token=207fed619d52d5a69fc5e153780160fb226c7f6b22365873763576dcb22204c5"
    url = "https://oapi.dingtalk.com/robot/send?access_token=ee82fa2fac51d325645dd8c5b7f27b756f1cdd7ab58fc7d0b63463fb296b59c9"
    data = {"msgtype": "markdown", "markdown": {"title": "Agent Domain ERROR", "text": info}, }
    header = {"Content-Type": "application/json"}
    r = requests.post(url, data=json.dumps(data), headers=header)


# 1. execute pytest command to a case
# 1.1 save printed results to logs
def runCase(case):
    f = os.popen(" ".join(["pytest", "-s", case, "2>&1"]))
    logs = f.read()
    f.close()
    return logs


# 2. collect all *.py to apiCases as a list
f = os.popen(" ".join(["ls", "/Users/jenniferjiang/QA/pythonProject/agentTest/house_agent/*.py"]))
apiCases = f.readlines()
f.close()
# 2.1 invoke runCase() in a for loop
for c in apiCases:
    logs = runCase(c.rstrip("\n"))
    if 'FAILED' in logs or 'ERROR' in logs:
        endWith1 = "_________________"
        endWith2 = "================="
        results = []
        pattern1 = re.compile(endWith2 + '.*' + endWith1, re.S)
        result1 = pattern1.findall(logs)
        if result1:
            results.extend(result1)
            # print results
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        info = "#### Agent Domain ERROR: " + '/'.join(c.split('/')[-2:])
        for r in results:
            # clean infomation
            # non-greedy mode to deal every one.
            pattern_clean1 = re.compile("test_" + '.*?' + 'TestSequense\)', re.S)
            pattern_clean2 = re.compile("Traceback" + ".*?" + 'AssertionError', re.S)
            # length compare has a huge content so that Dingding can not handle. Delete list comtent.
            pattern_clean3 = re.compile("\[" + ".*?" + "\]\(list\)\ length_", re.S)
            r = re.sub(pattern_clean1, '', r)
            r = re.sub(pattern_clean2, 'AssertionError', r)
            r = re.sub(pattern_clean3, '\[](list) length_', r)

            info = info + " > " + r.replace('-------', '').replace('=======', '').replace('\n', '\n > ')
            info = info + "###### " + t
            # print "******"+info
            sendDingAlert(info)

# def test():
# f = os.popen(" ".join(["ls", "/Users/jenniferjiang/QA/pythonProject/agentTest/house_agent/*.py"]))
# cases = f.readlines()
# f.close()
# for c in cases:
# print(runCase(c))


# test()
# case = "/Users/jenniferjiang/QA/pythonProject/agentTest/house_agent/test_main.py"
# for case in cases:

# print(runCase(case))
