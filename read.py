import requests
import sys
from channels import getChannels
from channels import getIMs
from errors import checkErrors
from users import getUsers
from utilities import colors
from utilities import printTable
from utilities import reverseMap

def readMessages(token, channel, count='10'):
    if channel[0] == '@': readIM(token, channel, count)
    else: readChannel(token, channel, count)


def readChannel(token, channel, count='10'):
    channelMap = getChannels(token, False)
    userIdMap = reverseMap(getUsers(token, False))

    if channel not in channelMap: sys.exit(colors.RED+'Error: '+channel+' is not a valid channel'+colors.ENDC)

    payload={'token':token, 'channel':channelMap[channel], 'count':count}
    r=requests.get('https://slack.com/api/channels.history', params=payload)

    data=r.json()
    checkErrors(data)

    info=[]
    for i in range(int(count)):
        info.append([userIdMap[data['messages'][i]['user']], data['messages'][i]['text']])

    printTable(list(reversed(info)), False)
    
def readIM(token, user, count='10'):
    userMap = getUsers(token, False)
    userIdMap = reverseMap(userMap)
    imMap = getIMs(token)

    if user not in userMap: sys.exit(colors.RED+'Error: '+user+' is not a valid user'+colors.ENDC)

    payload={'token':token, 'channel':imMap[userMap[user]], 'count':count}
    r=requests.get('https://slack.com/api/im.history', params=payload)

    data=r.json()
    checkErrors(data)

    info=[]
    for i in range(int(count)):
        info.append([userIdMap[data['messages'][i]['user']], data['messages'][i]['text']])

    printTable(list(reversed(info)), False)
