import requests
from .utilities import checkErrors

def sendFile(token, channel, message, file):
    files={'file':open(file,'rb')}
    payload={'token':token, 'channels':channel, 'initial_comment':message, 'as_user':'1'}
    r=requests.post('https://slack.com/api/files.upload', files=files, params=payload)
    checkErrors(r.json())

def sendMessage(token, channel, message):
    payload={'token':token, 'channel':channel, 'text':message, 'as_user':'1'}
    r=requests.post('https://slack.com/api/chat.postMessage', params=payload)
    checkErrors(r.json())
