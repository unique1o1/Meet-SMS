[![Build Status](https://travis-ci.org/unique1o1/Meet-SMS.svg?branch=master)](https://travis-ci.org/unique1o1/SMS)

# SimepleSMS

Meet-SMS is a python script for sending SMS using NTC Meet. This script makes it simple to send SMS without having to go to the site.

## Requirement

* **Python3**
* **Requests Module**

## Installation
* From GitHub

        git clone https://github.com/unique1o1/Meet-SMS
        cd Meet-SMS
        chmod 775 install.sh
        ./install.sh

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
