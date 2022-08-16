#Decoder System 

import logging

logging.basicConfig(filename = "decoder_test.log", level = logging.DEBUG, format = '%(message)s')

base_32 = "0123456789bcdefghjkmnpqrstuvwxyz"
base_dict = {}
for i in range(len(base_32)):
    base_dict[base_32[i]] = i

def decode(geohash:str):
    """takes a string geohash and converts the geohash to its corresponding latitude and longitude coordinates
    Input: geohash : string 
    Output: latitude : float, 
            longitude : float"""
    logging.debug(geohash)
    decimal_nums = []
    binary_nums = []
    dict_coordinates = {}
    for element in geohash:
        num = base_dict[element]
        decimal_nums.append(num)
        binary_nums.append(bin(num).replace("0b", ""))
    for i in range(len(binary_nums)):
        binary_nums[i] = binary_nums[i].rjust(5, '0')

    bin_string = ''.join(binary_nums)

    lon_string = bin_string[::2]
    lat_string = bin_string[1::2]

    lat_range = (-90.0, 90.0)
    lon_range = (-180.0, 180.0)
    final_lat = ""

    for i in range(len(lat_string)):
        lat_range = choose_interval(lat_range, lat_string[i])
        final_lat = (lat_range[0] + lat_range[1])/2
    
    for i in range(len(lon_string)):
        lon_range = choose_interval(lon_range, lon_string[i])
        final_lon = (lon_range[0] + lon_range[1])/2

    dict_coordinates["latitude"] = final_lat
    dict_coordinates["longitude"] = final_lon
    decimal_nums.clear()
    binary_nums.clear()
    logging.debug(dict_coordinates)

    return dict_coordinates


def choose_interval(range: tuple, num: str):
    mid_lat = (range[0] + range[1]) / 2
    interval_1 = (range[0],mid_lat)  # set lat_interval_1
    interval_2 = (mid_lat,range[1])  # set lat_interval_2
    if (num == "0"):
        range = interval_1
    elif (num == "1"):
        range = interval_2
    return range







