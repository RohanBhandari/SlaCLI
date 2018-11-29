import requests
from .utilities import checkErrors
from .utilities import colors
from .utilities import printTable

def getChannels(token, verbose=True):
    payload={'token':token, 'exclude_archived':'1'}
    r=requests.get('https://slack.com/api/channels.list', params=payload)

    data = r.json()
    checkErrors(data)

    channelMap = dict()
    if verbose: print(colors.header+'=== Channels ==='+colors.endc)
    for i in range(len(data['channels'])):
        if verbose: print(data['channels'][i]['name'])
        channelMap[data['channels'][i]['name']] = data['channels'][i]['id']

    return(channelMap)

def getIMs(token):
    payload={'token':token, 'exclude_archived':'1'}
    r=requests.get('https://slack.com/api/im.list', params=payload)

    data = r.json()
    checkErrors(data)

    imMap = dict()
    for i in range(len(data['ims'])):
        imMap[data['ims'][i]['user']] = data['ims'][i]['id']

    return(imMap)

def getUsers(token, verbose=True):
    payload={'token':token, 'presence':'1'}
    r=requests.get('https://slack.com/api/users.list', params=payload)

    data=r.json()
    checkErrors(data)

    info=[]
    info.append(['=== Username ===', '=== Name ===', '=== Presence ==='])
    userMap = dict()
    for i in range(len(data['members'])-1):
        if 'real_name' not in data['members'][i]:
            data['members'][i]['real_name'] = ''

        info.append(['@'+data['members'][i]['name'], data['members'][i]['real_name'], data['members'][i]['presence']])
        userMap['@'+data['members'][i]['name']] = data['members'][i]['id']
    userMap['BOT'] = 'BOT'

    if verbose:
        for row in info:
            if row[2] == 'active': row[2] = colors.green+row[2]+colors.endc
            elif row[2] == 'away': row[2] = colors.red+row[2]+colors.endc
                    
        printTable(info)
        
    return userMap
