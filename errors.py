import sys
from utilities import colors

def checkErrors(error):
    if error['ok'] == False: sys.exit(colors.RED + 'Error: ' + error['error'] + colors.ENDC)



