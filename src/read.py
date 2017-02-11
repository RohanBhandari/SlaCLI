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

def readMessages(token, channel, count='10'):
    if channel[0] == '@': readIM(token, channel, count)
    else: readChannel(token, channel, count)

def readChannel(token, channel, count='10'):
    channelMap = getChannels(token, False)
    userIdMap = reverseMap(getUsers(token, False))
    colorMap = makeColorMap(userIdMap)

    if channel not in channelMap: sys.exit(colors.RED+'Error: '+channel+' is not a valid channel'+colors.ENDC)

    payload={'token':token, 'channel':channelMap[channel], 'count':count}
    r=requests.get('https://slack.com/api/channels.history', params=payload)

    data=r.json()
    checkErrors(data)

    info=[]
    prevUser=''
    for i in range(int(count)):
        user = data['messages'][i]['user']
        newline = ''
        if user != prevUser: newline, prevUser = '\n', user

        info.append([colorMap[user]+userIdMap[user]+colors.ENDC, data['messages'][i]['text']+newline])

    printTable(list(reversed(info)), False)
    
def readIM(token, user, count='10'):
    userMap = getUsers(token, False)
    userIdMap = reverseMap(userMap)
    colorMap = makeColorMap(userIdMap)
    imMap = getIMs(token)

    if user not in userMap: sys.exit(colors.RED+'Error: '+user+' is not a valid user'+colors.ENDC)

    payload={'token':token, 'channel':imMap[userMap[user]], 'count':count}
    r=requests.get('https://slack.com/api/im.history', params=payload)

    data=r.json()
    checkErrors(data)

    info=[]
    prevUser=''
    for i in range(int(count)):
        user = data['messages'][i]['user']
        newline=''
        if user != prevUser: newline, prevUser = '\n', user
        info.append([colorMap[user]+userIdMap[user]+colors.ENDC, data['messages'][i]['text']+newline])

    printTable(list(reversed(info)), False)
