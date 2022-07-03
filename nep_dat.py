import osmnx as ox 

road = ox.graph_from_place('Kathmandu, Nepal', network_type = "drive")

prj_road = ox.project_graph(road)

ox.save_graph_shapefile(prj_road, filepath = '/Users/jasnabudhathoki/Desktop/geoHashing\kathmandu')




