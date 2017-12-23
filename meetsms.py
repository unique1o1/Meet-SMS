#! /usr/bin/env python3
import requests
import sys
import re
import getpass
for i in range(1, 7, 2):
    try:
        if(sys.argv[i] == "-u"):
            username = sys.argv[i + 1]

        elif (sys.argv[i] == "-m"):
            message = sys.argv[i + 1]
            print("jbvhj")
        elif (sys.argv[i] == "-r"):

            recipcent = sys.argv[i + 1].split(",")
            numbers = None
            for j in recipcent:
                j = j.strip()

                if re.match(r"^\d{10}$", j):
                    numbers = j if numbers is None else numbers + "," + j
                else:
                    raise ValueError("The number you entered is mistake")
                    exit()

    except IndexError as e:
        print("not enough arguments \n{}".format(e))
        exit()

password = getpass.getpass("Enter your password: ")
login_url = "http://www.meet.net.np/meet/action/login"
sms_url = "http://www.meet.net.np/meet/mod/sms/actions/send.php"
session_req = requests.session()
print("Sending SMS...")
data = {
    "username": username,
    "password": password,

}


messages = {"recipient": numbers,
            "message": message,
            "SmsLanguage": "English",
            "sendbutton": "Send Now"}
resp = session_req.post(login_url, data)
result = session_req.post(sms_url, messages)
html_ = str(result.content)
index_ = re.search("Free SMS Quota", html_)
if index_:
    Quota = html_[index_.start():index_.start() + 46]
    print("Success.\n" + Quota)
else:
    print("Either your out of Quota or something went wrong.")
