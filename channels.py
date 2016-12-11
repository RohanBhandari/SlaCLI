import json
import os
import requests

def getChannels():
    payload={'token':os.environ.get('SLACK_TOKEN'), 'exclude_archived':'1'}
    r=requests.get('https://slack.com/api/channels.list', params=payload)

    data = r.json()
    channelMap = dict()
    for i in range(len(data['channels'])):
        print(data['channels'][i]['name'])
        channelMap[data['channels'][i]['name']] = data['channels'][i]['id']

    return(channelMap)
