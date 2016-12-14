import requests
from errors import checkErrors
from utilities import colors

def getChannels(token, verbose=True):
    payload={'token':token, 'exclude_archived':'1'}
    r=requests.get('https://slack.com/api/channels.list', params=payload)

    data = r.json()
    checkErrors(data)

    channelMap = dict()
    if verbose: print(colors.HEADER+'=== Channels ==='+colors.ENDC)
    for i in range(len(data['channels'])):
        if verbose: print(data['channels'][i]['name'])
        channelMap[data['channels'][i]['name']] = data['channels'][i]['id']

    return(channelMap)
