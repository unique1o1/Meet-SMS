# SimepleSMS

SimpleSMS is a python script for sending SMS using NTC Meet. This script makes it simple to send SMS without having to go to the site.

## Requirement

* **Python3**
* **Requests Module**

## Installation

        git clone https://github.com/unique1o1/SimpleSMS
        cd SimpleSMS
        chmod 775 install.sh
        ./install

##### Syntax

`-u` for username
`-p` for password
`-m` for message
`-r` for receiver's number

## How to use

First lets make an _alias_ so, we don't have to type _username_ and _password_ everytime.
In your terminal type:

> sudo nano ~/.bashrc

##### Add the following to the end of your file

> alias sms="sms -u yourusername -p yourpassword"

##### Sending SMS

> sms -r 98**\*\*\*\*** -m "message"

#### Sending sms to multiple people

> sms -r "98**\*\*\*\***, 98**\*\*\*\***" -m "message"
