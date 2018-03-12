[![Build Status](https://travis-ci.org/unique1o1/Meet-SMS.svg?branch=master)](https://travis-ci.org/unique1o1/SMS)
[![Code Climate](https://api.codeclimate.com/v1/badges/dd62ac0f1807796eab52/maintainability.svg)](https://github.com/unique1o1/Meet-SMS)
# MEETSMS

Meet-SMS is a python script for sending SMS using NTC Meet. This script makes it simple to send SMS without having to go to the site.

## Requirement

* **Python3**
* **Requests**

## Installation
* From Source

        git clone https://github.com/unique1o1/Meet-SMS
        cd Meet-SMS
        sudo setup.py install
    

* From PIP

        sudo pip install meetsms
        
##### Syntax

`-u` for username
`-m` for message
`-r` for receiver's number

## How to use

First lets make an _alias_ so, we don't have to type _username_ everytime.
In your terminal type:

> sudo nano ~/.bashrc for bash users

> sudo nano ~/.zshrc for zsh users

##### Add the following to the end of your file

> alias sms="sms -u yourusername"

##### Sending SMS

> sms -r 98**\*\*\*\*** -m "message"

#### Sending sms to multiple people

> sms -r "98**\*\*\*\***, 98**\*\*\*\***" -m "message"
