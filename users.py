import requests
from errors import checkErrors
from utilities import colors
from utilities import printTable

def getUsers(token):
    payload={'token':token, 'presence':'1'}
    r=requests.get('https://slack.com/api/users.list', params=payload)

    data=r.json()
    checkErrors(data)

    info=[]
    info.append(['=== Username ===', '=== Name ===', '=== Presence ==='])
    for i in range(len(data['members'])-1):
        info.append(['@'+data['members'][i]['name'], data['members'][i]['real_name'], data['members'][i]['presence']])

    for row in info:
        if row[2] == 'active': row[2] = colors.GREEN+row[2]+colors.ENDC
        elif row[2] == 'away': row[2] = colors.RED+row[2]+colors.ENDC
                    
    printTable(info)
        

