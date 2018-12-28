import re


#DMS to DD in one function
def dms_to_dd_1(dms):
    parts = re.split('[^\d\w]+', dms)  # splits the degree, ', and " symbols
    deg = float(parts[0])
    min = float(parts[1])
    sec = float(parts[2])
    if parts[3] == 'W' or parts[3] == 'S':
        return -1 * (deg + (min / 60) + (sec / 3600))
    else:
        return deg + (min / 60) + (sec / 3600)

#DMS to DD with two functions

#Parses the DMS coord into four parts, deg
def parse_dms(dms):
    return re.split('[^\d\w]+', dms) #splits the degree, ', and " symbols

def dms_to_dd(deg,min,sec,direc):
    if direc == 'W' or direc == 'S':
        return -1 * (deg + (min / 60) + (sec / 3600))
    else:
        return deg + (min / 60) + (sec / 3600)

