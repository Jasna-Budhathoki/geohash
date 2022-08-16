# Geohash_encoder using ward boundaries
from turfpy.measurement import boolean_point_in_polygon
from geojson import Point, Feature
import os
import geojson

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "pokhara-ward.geojson")
with open(file_path) as f:
    gj = geojson.load(f)
features = gj["features"]

admin_geohash = []


def ward_info(lat, long):
    """Takes latitude and longitude coordinates and returns the name of the city and ward number if the point is within the boundary of the city
    Input: latitude : float, longitude : float
    Output: Returns the name of the city and the ward number the point is located in"""
    location_point = Feature(geometry=Point([long, lat]))  # long,lat
    in_pokhara = False
    for i in range(len(features)):
        bool_true = boolean_point_in_polygon(location_point, features[i])
        if bool_true:
            admin_geohash.clear()
            features_dict = gj["features"][i]["properties"]
            name = features_dict.get("name")
            admin_geohash.append(name.split()[0])
            admin_geohash.append(name.rpartition(" ")[-1])
            in_pokhara = True
            return admin_geohash
    if in_pokhara == False:
        print("The point with lat %f and %f is not in Pokhara " % (lat, long))
        return -1
