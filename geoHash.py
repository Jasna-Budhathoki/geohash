from math import log10

#  Note: the alphabet in geohash differs from the common base32 alphabet described in IETF's RFC 4648
# (http://tools.ietf.org/html/rfc4648)

__base32 = '0123456789bcdefghjkmnpqrstuvwxyz'
__decodemap = dict()
for i in range(len(__base32)):
    __decodemap[__base32[i]] = i

print(__decodemap)


def decode_exactly(geohash):
    """
    Decode the geohash to its exact values, including the error
    margins of the result.  Returns four float values: latitude,
    longitude, the plus/minus error for latitude (as a positive
    number) and the plus/minus error for longitude (as a positive
    number).
    """
    lat_interval, lon_interval = (-90.0, 90.0), (-180.0, 180.0)
    lat_err, lon_err = 90.0, 180.0
    is_even = True
    for c in geohash:
        cd = __decodemap[c]
        print ("cd",cd)
        for mask in [16, 8, 4, 2, 1]:
            print("mask",mask)
            if is_even: # adds longitude info
                lon_err /= 2
                print("cd & mask", cd & mask)
                if cd & mask:
                    lon_interval = ((lon_interval[0]+lon_interval[1])/2, lon_interval[1])
                    print("lon_interval 1",lon_interval)
                else:
                    lon_interval = (lon_interval[0], (lon_interval[0]+lon_interval[1])/2)
                    print("lon_interval 2",lon_interval)
            else:      # adds latitude info
                lat_err /= 2
                if cd & mask:
                    lat_interval = ((lat_interval[0]+lat_interval[1])/2, lat_interval[1])
                    print("lat_interval 1",lat_interval)
                else:
                    lat_interval = (lat_interval[0], (lat_interval[0]+lat_interval[1])/2)
                    print("lat_interval 2",lat_interval)
            is_even = not is_even
            print("is_even",is_even)
    lat = (lat_interval[0] + lat_interval[1]) / 2
    lon = (lon_interval[0] + lon_interval[1]) / 2
    print (lat, lon, lat_err, lon_err)
    return lat, lon, lat_err, lon_err



decode_exactly('ezs42')