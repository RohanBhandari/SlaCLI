# SlaCLI

A Command Line Interface (CLI) for Slack -- read, send, and manage your Slack channels from the command line!

* [Usage](#usage)
  * [List](#list)
  * [Read](#read)
  * [Send](#send)
* [Installation](#installation)
* [Suggested Shortcuts](#suggested-shortcuts)

![Alt text](/../example/example.jpg?raw=true "SlaCLI in motion!")

## Usage
SlaCLI is divided into three main functionalities: `list`, `read`, and `send`. 

```
usage: slacli.py [-h] [-t TOKEN] {list,read,send} ...

Read and send your Slack messages over the command line!

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Use specified token instead of $SLACK_TOKEN

Commands:
  {list,read,send}
    list                List channels and users
    read                Read messages from a channel
    send                Send a message
```

###List
Using `./slacli.py list` will print your Slack team's public channels followed by the team users and their online presence. 
Adding the `-c` or `-u` flag will limit the output to only channels or users, respectively.

```
usage: slacli.py list [-h] [-c | -u]

optional arguments:
  -h, --help      show this help message and exit
  -c, --channels  List only channels
  -u, --users     List only users
```
  
###Read
Using `./slacli.py read [channel] [num]` will print recent messages from a channel or direct messages with another user. 
For channels, simply provide the channel name, while for users, use their username (including the "@"). 
By default, SlaCLI will show the last ten messages, unless a value for `num` is specified.

```
usage: slacli.py read [-h] [-u UNREAD] channel [num]

positional arguments:
  channel               The channel or user to read from
  num                   Number of messages to display. Default is 10

optional arguments:
  -h, --help            show this help message and exit
  -u UNREAD, --unread UNREAD
                        Show only unread messages
```

###Send
Using `./slacli.py send [channel] [message]` will send a message to a channel or directly to a user. 
The same convention applies for `channel` as stated for the read functionality. 
The `message` argument can be provided as a string using either single or double quotes.

```
usage: slacli.py send [-h] channel message

positional arguments:
  channel     The channel or user to send the message to
  message     The message text

optional arguments:
  -h, --help  show this help message and exit
```

##Installation 
Simply clone the SlaCLI repository!
The only dependency needed is [requests](http://docs.python-requests.org/en/master/), which can be easily installed with pip:
```
pip install requests
```

##Suggested Shortcuts
To make using SlaCLI easier, here are some suggested shortcuts to use:
```
alias sl='python ~/PATH/SlaCLI/slacli.py list'
```
```
alias sr='python ~/PATH/SlaCLI/slacli.py read'
```
```
alias ss='python ~/PATH/SlaCLI/slacli.py send'
```
```
alias srg='python ~/PATH/SlaCLI/slacli.py read general'
```
```
alias ssb='python ~/PATH/SlaCLI/slacli.py send @bob'
```
