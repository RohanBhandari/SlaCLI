import sys

def checkErrors(error):
    if error['ok'] == False: sys.exit('\033[31m'+'Error: ' + error['error'] + '\033[0m')



