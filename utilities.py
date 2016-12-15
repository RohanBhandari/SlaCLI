class colors:
    HEADER = '\033[95m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    ENDC = '\033[0m'

def printTable(info, header=True):

    row_format = ''
    zippedInfo = zip(*info)
    for row in range(len(zippedInfo)):
        # Added extra buffer of 5 spaces
        row_format += '{:<'+str(len(max(zippedInfo[row],key=len))+5)+'}' if row != len(zippedInfo)-1 else '{:<}'

    for i in range(len(info)):
        if header and i==0: 
            print(colors.HEADER+row_format.format(*info[i])+colors.ENDC)
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
