
'''
Meet-SMS - Send SMS easily from MeetSMS

Author: Yunik Maharjan
'''
# from __future__ import print_function
import requests
import sys
import re
import itertools
import threading
import time
import getpass


def main():

    global done
    done = False
    for i in range(1, 7, 2):
        try:
            if(sys.argv[i] == "-u"):
                username = sys.argv[i + 1]

            elif (sys.argv[i] == "-m"):
                message = sys.argv[i + 1]

            elif (sys.argv[i] == "-r"):

                recipcent = sys.argv[i + 1].split(",")
                if len(recipcent) > 10:
                    print("Sending more than 10 SMS is not supported.")
                    exit()
                numbers = None
                ncell = None
                for j in recipcent:
                    j = j.strip()
                    # Check for Ncell numbers
                    if re.match(r"^\d{10}$", j):
                        if(int(j) >= 9800000000 and int(j) <= 9829999999):
                            ncell = j if ncell is None else ncell + "," + j
                        else:
                            numbers = j if numbers is None else numbers + "," + j
                    else:
                        raise ValueError("The number you entered is mistake")
                        exit()

        except IndexError as e:
            print("not enough arguments \n  Use the following options:\n -u for username \n -m for message \n -r for receiver's number".format(e))
            exit()

    password = getpass.getpass("Enter your password: ")
    login_url = "http://www.meet.net.np/meet/action/login"
    sms_url = "http://www.meet.net.np/meet/mod/sms/actions/send.php"
    session_req = requests.session()

    data = {
        "username": username,
        "password": password,

    }

    try:

        messages = {"recipient": numbers,
                    "message": message,
                    "SmsLanguage": "English",
                    "sendbutton": "Send Now"}
    except NameError as e:
        print("Error! {}\nUse the following options:\n -u for username \n -m for message \n -r for receiver's number".format(e))
        exit()

    t = threading.Thread(target=animate)
    t.start()

    resp = session_req.post(login_url, data)
    result = session_req.post(sms_url, messages)
    html_ = str(result.content)
    index_ = re.search("Free SMS Quota", html_)
    done = True
    if index_:
        Quota = html_[index_.start():index_.start() + 46]
        print("\rSuccess\n" + Quota)
        if ncell is not None:
            print(
                "SMS to {} was not send because Ncell numbers are not supported".format(ncell))
    elif re.search("loginform", html_):
        print("\rThe username/password you entered in incorrect")
    else:
        print(
            "\rSMS to {} was not send because Ncell numbers are not supported".format(ncell))
        print("Or Either your out of Quota or something went wrong.")


def unit_test(text):
    return text


def animate():

    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rSending ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.flush()


if __name__ == '__main__':
    main()
