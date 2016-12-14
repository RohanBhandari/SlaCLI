import json
import os
import requests
from errors import checkErrors

def getChannels(token, verbose=True):
    payload={'token':token, 'exclude_archived':'1'}
    r=requests.get('https://slack.com/api/channels.list', params=payload)

    data = r.json()
    checkErrors(data)

    channelMap = dict()
    if verbose: print('\033[95m'+'=== Channels ==='+'\033[0m')
    for i in range(len(data['channels'])):
        if verbose: print(data['channels'][i]['name'])
        channelMap[data['channels'][i]['name']] = data['channels'][i]['id']

    return(channelMap)
