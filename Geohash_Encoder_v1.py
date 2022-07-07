#Jasna Budhathoki
#Geohash - encoder
#Program that converts lat,long to geohash 
#July 3, 2022

from geohash_encoder_turf import *

base_32 = "0123456789bcdefghjkmnpqrstuvwxyz"
base_dict = {}
for i in range(len(base_32)):
    base_dict[base_32[i]] = i

def encode(lat, lon):
    interval = []
    interval_lon = []
    count = 0
    lat_range = (-90.0, 90.0)
    # set two intervals based on the given lat_range
    mid_lat = (lat_range[0] + lat_range[1]) / 2
    lat_interval_1 = (lat_range[0],mid_lat)  # set lat_interval_1
    lat_interval_2 = (mid_lat,lat_range[1])  # set lat_interval_2
    #set two intervals based on the given lon_range
    lon_range = (-180.0, 180.0)
    mid_lon = (lon_range[0] + lon_range[1]) / 2
    lon_interval_1 = (lon_range[0],mid_lon)  # set lon_interval_1
    lon_interval_2 = (mid_lon,lon_range[1])  # set lon_interval_2
    
    #for latitude

    while (count < 20):
        if (lat > lat_interval_1[0]) and (lat < lat_interval_1[1]):
            interval.append('0')
            mid_lat_interval = (lat_interval_1[0] + lat_interval_1[1]) / 2
            lat_interval_2 = (mid_lat_interval, lat_interval_1[1])  # set lat_interval_2
            lat_interval_1 = (lat_interval_1[0], mid_lat_interval)

        elif (lat > lat_interval_2[0]) and (lat < lat_interval_2[1]):
            interval.append('1')
            mid_lat_interval = (lat_interval_2[0] + lat_interval_2[1]) / 2
            lat_interval_1 = (lat_interval_2[0],mid_lat_interval)  # set lat_interval_1
            lat_interval_2 = (mid_lat_interval,lat_interval_2[1])
        count += 1

    #for longitude

    count = 0
    while (count < 20):
        if (lon > lon_interval_1[0]) and (lon < lon_interval_1[1]):
            interval_lon.append('0')
            mid_lon_interval = (lon_interval_1[0] + lon_interval_1[1]) / 2
            lon_interval_2 = (mid_lon_interval, lon_interval_1[1])  # set lon_interval_2
            lon_interval_1 = (lon_interval_1[0], mid_lon_interval)

        elif (lon > lon_interval_2[0]) and (lon < lon_interval_2[1]):
            interval_lon.append('1')
            mid_lon_interval = (lon_interval_2[0] + lon_interval_2[1]) / 2
            lon_interval_1 = (lon_interval_2[0],mid_lon_interval)  # set lon_interval_1
            lon_interval_2 = (mid_lon_interval,
                lon_interval_2[1])
        count += 1
    
    list3 = []
    #alternate between lon and lat interval lists
    while True:
        try:
            list3.append(interval_lon.pop(0))
            list3.append(interval.pop(0))
        except IndexError:
            break

    str = ''.join(list3)

    n = 5
    chunks = [str[i:i+n] for i in range(0, len(str), n)]
    key_list = list(base_dict.keys())
    val_list = list(base_dict.values())

    geohash = ""
    for i in range(len(chunks)):
        x = int(chunks[i], 2)
        position = val_list.index(x)
        geohash = geohash + key_list[position]
    admin_info = ward_info(lat,lon)
    if (admin_info == -1):
        return "not in pokhara"
    #print("admin_info",admin_info)
    final_geohash = ""
    final_geohash = admin_info[0]+ admin_info[1] + "-" + geohash[-3:]
    print ("The ward level geohash is",final_geohash)
    print("The 8 digit geohash is",geohash)
    return geohash

encode(28.1472,84.0823) #Pokhara University ward 30 
encode(28.1739,84.0973) #Begnas Lake ward 31
encode(28.2067,83.9816) #Phewa City hospital ward 8
encode(28.2118,83.9814) #Metro City hospital ward 8
encode(28.2180345,83.9794506) #random point 

