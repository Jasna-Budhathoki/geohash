#Jasna Budhathoki
#geohash_encoder using ward boundaries 

from turfpy.measurement import boolean_point_in_polygon
from geojson import Point, Feature

import geojson
with open('/Users/jasnabudhathoki/Desktop/geoHashing/pokhara-ward.geojson') as f:
    gj = geojson.load(f)
features = gj['features']
#print(features)

admin_geohash = []

def ward_info(lat,long):
    point = Feature(geometry=Point([long,lat])) #long,lat
    in_pokhara = False
    for i in range(len(features)):
        bool_true = boolean_point_in_polygon(point,features[i])
        if (bool_true):
            admin_geohash.clear()
            dict = gj["features"][i]["properties"]
            name = dict.get("name")
            admin_geohash.append(name.split()[0])
            admin_geohash.append(name.rpartition(' ')[-1])
            in_pokhara = True
            return admin_geohash
    if in_pokhara == False:
        print("The point with lat %f and %f is not in Pokhara " %(lat,long))
        return -1
    


        


    


