import re

#User input
# coord=input('Enter coordinate: ')
coord_dms="42°24′31.32″N"
coord_dd=-42.408699999999996


#DMS to DD
def dd_calc(deg,min,sec,direc):#Parses the DMS coord into four parts, deg
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


#DD to DMS
def dd_to_dms(dd,direction):
    deg=int(dd)
    minDec= (dd-deg)*60
    minutes = int(minDec)
    sec = (minDec-minutes)*60

    Geo_coord={"lon":('N','S'),
               "lat":('W','E')
    }

    return "{}°{}′{}″{}" .format(abs(deg), abs(minutes), abs(sec),Geo_coord[direction][0 if deg>0 else 1])



print(dd_to_dms(coord_dd,'lat'))
new_coord=dd_to_dms(coord_dd,'lon')


