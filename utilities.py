def printTable(info, header=True):

    row_format = ''
    for row in zip(*info):
        #Added extra buffer of 5 spaces
        row_format += '{:<'+str(len(max(row,key=len))+5)+'}'

    for i in range(len(info)):
        if header and i==0: print(colors.HEADER+row_format.format(*info[i])+colors.ENDC)
        else: print(row_format.format(*info[i]))


class colors:
    HEADER = '\033[95m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    ENDC = '\033[0m'    

    
