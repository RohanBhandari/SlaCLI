import requests
import sys
from list import getChannels
from list import getIMs
from list import getUsers
from utilities import colors
from utilities import checkErrors
from utilities import makeColorMap
from utilities import printTable
from utilities import reverseMap

def readMessages(token, channel, count='10', unread=False):
    #Check whether to read channel or IM and use appropriate method
    if channel[0] == '@': readIM(token, channel, count, unread)
    else: readChannel(token, channel, count, unread)

def readChannel(token, channel, count='10', unread=False):
    #Get necessary information
    channelMap = getChannels(token, False)
    userIdMap = reverseMap(getUsers(token, False))
    colorMap = makeColorMap(userIdMap)

    #Check if channel is valid
    if channel not in channelMap: sys.exit(colors.red+'Error: '+channel+' is not a valid channel'+colors.endc)
    #If only want unread messages, get enough messages to be a superset of the unread messages
    if unread: count = 200

    #Setup and send request
    payload={'token':token, 'channel':channelMap[channel], 'count':count, 'unreads':'true'}
    r=requests.get('https://slack.com/api/channels.history', params=payload)
    data=r.json()
    checkErrors(data)

    #If only want unread messages, set count to number of unread messages
    if unread: 
        count = int(data['unread_count_display'])
        if count==0: sys.exit(colors.green + 'No unread messages' + colors.endc)

    #Get messsage information
    info, prevUser = [], ''
    for i in range(int(count)):
        user, message = '', ''
        if 'user' in data['messages'][i]: 
            user = data['messages'][i]['user']
            message = data['messages'][i]['text']
        elif 'bot_id' in data['messages'][i]:
            user = 'BOT'
            message = data['messages'][i]['attachments'][0]['text']
        else:
            print(colors.red + 'Error: Could not read message. Skipping.' + colors.endc)
            continue

        newline = ''
        if user != prevUser: newline, prevUser = '\n', user

        info.append([colorMap[user]+userIdMap[user]+colors.endc, message+newline])

    printTable(list(reversed(info)), False)
    
    markChannelRead(token, channelMap[channel], data['messages'][0]['ts'])

def readIM(token, user, count='10', unread=False):
    #Get necessary information
    userMap = getUsers(token, False)
    userIdMap = reverseMap(userMap)
    colorMap = makeColorMap(userIdMap)
    imMap = getIMs(token)
    
    #Check if username is valid
    if user not in userMap: sys.exit(colors.red+'Error: '+user+' is not a valid user'+colors.endc)
    #If only want unread messages, get enough messages to be a superset of the unread messages
    if unread: count = 200

    #Setup and send request
    payload={'token':token, 'channel':imMap[userMap[user]], 'count':count, 'unreads':'true'}
    r=requests.get('https://slack.com/api/im.history', params=payload)
    data=r.json()
    checkErrors(data)

    #If only want unread messages, set count to number of unread messages
    if unread: 
        count = int(data['unread_count_display'])
        if count==0: sys.exit(colors.green + 'No unread messages' + colors.endc)

    #Get messsage information
    info, tmpUser, prevUser = [], user, ''
    for i in range(int(count)):
        tmp_user = data['messages'][i]['user']
        newline=''
        if tmp_user != prevUser: newline, prevUser = '\n', tmp_user
        info.append([colorMap[tmp_user]+userIdMap[tmp_user]+colors.endc, data['messages'][i]['text']+newline])

    printTable(list(reversed(info)), False)

    markIMRead(token, imMap[userMap[user]], data['messages'][0]['ts'])

def markChannelRead(token, channel, timestamp):
    payload={'token':token, 'channel':channel,'ts':timestamp}
    r=requests.post('https://slack.com/api/channels.mark', params=payload)

def markIMRead(token, channel, timestamp):
    payload={'token':token, 'channel':channel,'ts':timestamp}
    r=requests.post('https://slack.com/api/im.mark', params=payload)
