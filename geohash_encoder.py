#Jasna Budhathoki
#Geohash - encoder
#Program that converts lat,long to geohash 
#July 3, 2022

from geohash_encoder_turf import *

base_32 = "0123456789bcdefghjkmnpqrstuvwxyz"
base_dict = {}
for i in range(len(base_32)):
    base_dict[base_32[i]] = i

def choose_interval(interval_1, interval_2, coordinate, interval):
    if (coordinate > interval_1[0]) and (coordinate < interval_1[1]):
        interval += "0"
        mid_interval = (interval_1[0] + interval_1[1]) / 2
        interval_2 = (mid_interval, interval_1[1])  # set interval_2
        interval_1 = (interval_1[0], mid_interval) #set interval_1

    elif (coordinate > interval_2[0]) and (coordinate < interval_2[1]):
        interval += "1"
        mid_interval = (interval_2[0] + interval_2[1]) / 2
        interval_1 = (interval_2[0],mid_interval) # set interval_1
        interval_2 = (mid_interval,interval_2[1]) # set interval_2
        
    return interval,interval_1,interval_2

def encode(lat, lon):
    interval_lat = ""
    interval_lon = ""

    count = 0
    lat_interval_1 = (-90.0,0.0)  # set lat_interval_1
    lat_interval_2 = (0.0,90.0)  # set lat_interval_2
    lon_interval_1 = (-180.0,0.0)  # set lat_interval_1
    lon_interval_2 = (0.0,180.0)  # set lat_interval_2

    #to update lat intervals and lon intervals
    while (count < 20):
        updates_lat = choose_interval(lat_interval_1, lat_interval_2, lat, interval_lat)
        lat_interval_1 = updates_lat[1]
        lat_interval_2 = updates_lat[2]
        interval_lat = updates_lat[0]
        updates_lon = choose_interval(lon_interval_1, lon_interval_2, lon, interval_lon)
        lon_interval_1 = updates_lon[1]
        lon_interval_2 = updates_lon[2]
        interval_lon = updates_lon[0]
        count += 1

    str = ''.join(map(''.join, zip(interval_lon,interval_lat)))  # kudos @Coldspeed
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