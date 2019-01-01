import re

#User input
# coord=input('Enter coordinate: ')
coord="42°24′31.32″N"
answer=42.408699999999996


#DMS to DD in one function
def dms_to_dd_1(dms):
    parts = re.split('[^\d\w]+', dms)#Splits all symbols except for integers and unicode characters

    if len(parts)>4:
        deg = int(parts[0])
        min = int(parts[1])
        sec = int(parts[2])+(int(parts[3])/100)#Correction of the decimal split
        if parts[4] == 'W' or parts[4] == 'S':
            return -1 * (deg + (min / 60) + (sec / 3600))
        else:
            return deg + (min / 60) + (sec / 3600)

    else:
        deg = int(parts[0])
        min = int(parts[1])
        sec = int(parts[2])
        if parts[3] == 'W' or parts[3] == 'S':
            return -1 * (deg + (min / 60) + (sec / 3600))
        else:
            return deg + (min / 60) + (sec / 3600)

#DMS to DD with two functions

#Parses the DMS coord into four parts, deg

def dd_calc(deg,min,sec,direc):
    if direc == 'W' or direc == 'S':
        return -1 * (deg + (min / 60) + (sec / 3600))
    else:
        return deg + (min / 60) + (sec / 3600)


def dms_to_dd(dms):
    parts = re.split('[^\d\w]+', dms)#Splits all symbols except for integers and unicode characters

    if len(parts)>4:#This statement accounts for a parsing of decimals
        return dd_calc(int(parts[0]), int(parts[1]), (int(parts[2])+(int(parts[3])/100)), parts[4])
    else:
        return dd_calc(int(parts[0]), int(parts[1]), int(parts[2]), parts[3])


print(dms_to_dd(coord))
