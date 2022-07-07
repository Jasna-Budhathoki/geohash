#Jasna Budhathoki
# July 6, 2022
# decoder system

#Decoder algorithm

# create a dict with base_32
# map the keys to values to get the decimal numbers
# convert the decimal numbers to binary for both lat and long 
# add the odd digits to long 
# add the even digits to lat 
# divide the lat range from (-90,90) and choose the interval based on whether the digit is 0 or 1
# divide the lon range from (-180,180) and choose the interval based on whether the digit is 0 or 1
# get the midpoint of the final range
# print lat and long 

base_32 = "0123456789bcdefghjkmnpqrstuvwxyz"
base_dict = {}
for i in range(len(base_32)):
    base_dict[base_32[i]] = i

decimal_nums = []
binary_nums = []

def decode(geohash:str):
    for element in geohash:
        num = base_dict[element]
        decimal_nums.append(num)
        binary_nums.append(bin(num).replace("0b", ""))
    for i in range(len(binary_nums)):
        binary_nums[i] = binary_nums[i].rjust(5, '0')
    #print(binary_nums)

    bin_string = ''.join(binary_nums)

    lon_string = bin_string[::2]
    lat_string = bin_string[1::2]

    lat_range = (-90.0, 90.0)
    lon_range = (-180.0, 180.0)
    final_lat = ""

    for i in range(len(lat_string)):
        lat_range = choose_interval(lat_range, lat_string[i])
        final_lat = (lat_range[0] + lat_range[1])/2
    print("final_lat",final_lat)

    
    for i in range(len(lon_string)):
        lon_range = choose_interval(lon_range, lon_string[i])
        final_lon = (lon_range[0] + lon_range[1])/2
    print("final_lon",final_lon)


def choose_interval(range: tuple, num: str):
    mid_lat = (range[0] + range[1]) / 2
    interval_1 = (range[0],mid_lat)  # set lat_interval_1
    interval_2 = (mid_lat,range[1])  # set lat_interval_2
    if (num == "0"):
        range = interval_1
    elif (num == "1"):
        range = interval_2
    return range

    #print(decimal_nums)

#decode('tv5b1k4c') #28.1472,84.0823
#decode('tv5b38vu') #28.1739,84.0973
#decode('tv58rnce') #28.2067,83.9816
#decode('tv58rpc3') #28.2118,83.9814
#decode('tv58wbzv') #28.2180345,83.9794506
#decode("tv58x1eu") #28.2219584,83.9848687
#decode('tv58tfdc') #28.2268938,83.9284967
#decode('tv58xm8n') #28.2441583,83.9907042

#Difference between encoder and decoder
#3.759m
#3.391m
#13.954m
#15.533m
#8.198m
#1.8474m
#8.562m









