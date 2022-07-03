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
    mid_lat = lat_range[0] + lat_range[1] / 2
    lat_interval_1 = (lat_range[0],mid_lat)  # set lat_interval_1
    lat_interval_2 = (mid_lat,lat_range[1])  # set lat_interval_2
    #set two intervals based on the given lon_range
    lon_range = (-180.0, 180.0)
    mid_lon = lon_range[0] + lon_range[1] / 2
    lon_interval_1 = (lon_range[0],mid_lon)  # set lon_interval_1
    lon_interval_2 = (mid_lon,lon_range[1])  # set lon_interval_2

    #for latitude

    while (count < 20):
        if (lat > lat_interval_1[0]) and (lat < lat_interval_1[1]):
            interval.append('0')
            mid_lat_interval = lat_interval_1[0] + lat_interval_1[1] / 2
            lat_interval_2 = (mid_lat_interval, lat_interval_1[1])  # set lat_interval_2
            lat_interval_1 = (lat_interval_1[0], mid_lat_interval)

        elif (lat > lat_interval_2[0]) and (lat < lat_interval_2[1]):
            interval.append('1')
            mid_lon_interval = (lat_interval_2[0] + lat_interval_2[1]) / 2
            lat_interval_1 = (lat_interval_2[0],mid_lon_interval)  # set lat_interval_1
            lat_interval_2 = (mid_lon_interval,
                lat_interval_2[1])
        count += 1

    #for longitude

    count = 0
    while (count < 20):
        if (lon > lon_interval_1[0]) and (lon < lon_interval_1[1]):
            interval_lon.append('0')
            mid_lon_interval = lon_interval_1[0] + lon_interval_1[1] / 2
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
    geohash = ''
    key_list = list(base_dict.keys())
    val_list = list(base_dict.values())
    for i in range(len(chunks)):
        x = int(chunks[i], 2)
        position = val_list.index(x)
        geohash += key_list[position]
    print(geohash)

encode(39.92324, 116.3906)
encode(74.34552,-78.6474)
encode(-78.4568,88.5637)


