import requests

def sendMessage(token, channel, message):
    payload={'token':token, 'channel':channel, 'text':message, 'as_user':'1'}
    r=requests.get('https://slack.com/api/chat.postMessage', params=payload)
