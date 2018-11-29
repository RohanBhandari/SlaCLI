import sys

class colors:
    header = '\033[95m'
    black = '\033[30m'
    blue = '\033[34m'    
    green = '\033[32m'
    cyan = '\033[36m'
    red = '\033[31m'
    purple = '\033[35m'
    brown = '\033[33m'
    grey = '\033[37m'
    endc = '\033[0m'

    list = [blue, purple, green, grey, brown, grey, red, cyan]

def printTable(info, header=True):

    row_format = ''
    zippedInfo = list(zip(*info))
    for row in range(len(zippedInfo)):
        # Added extra buffer of 5 spaces
        row_format += '{:<'+str(len(max(zippedInfo[row],key=len))+5)+'}' if row != len(zippedInfo)-1 else '{:<}'

    for i in range(len(info)):
        if header and i==0: 
            print(colors.header+row_format.format(*info[i])+colors.endc)
        else:
            try:
                print(row_format.format(*info[i]))
            except UnicodeEncodeError:
                # Replace the "Smart (single) Quotes" with "Dumb Quotes"
                for j in range(len(info[i])): info[i][j] = info[i][j].replace(u'\u2018','\'').replace(u'\u2019','\'').replace(u'\u201c','"').replace(u'\u201d','"')
                try:
                    print(row_format.format(*info[i]))
                except UnicodeEncodeError:
                    # In case there were some characters that were not replaced
                    for j in range(len(info[i])): info[i][j] = info[i][j].encode('ascii','replace')
                    print(row_format.format(*info[i]))
                      
def reverseMap(map):
    reversedMap = {v: k for k, v in map.items()}
    return reversedMap

def makeColorMap(map):    
    colorMap = {list(map.keys())[i] : colors.list[i % len(colors.list)] for i in range(len(map.keys()))}
    return colorMap

def checkErrors(error):
    if error['ok'] == False: sys.exit(colors.red + 'Error: ' + error['error'] + colors.endc)
