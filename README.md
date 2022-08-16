# Geohash Encoder and Decoder 
This projects contains a geohash encoder and a geohash decoder. Learn more about Geohash below! 

## What is Geohash

A geohash is a convenient way of expressing a location using a short alphanumeric string. As the geohash strings gets longer, the location can be obtained with greater precision. 

For example, a point with latitude 48.669 and longitude 45.56116 can be converted to a geohash of 'v08kugbt' when expressed in an 8 digits precision. 

### Geohash Encoder

Geohash Encoder coverts a tuple of latitude and longitude to its corresponding geohash. This program converts a given latitude and longitude to an 8 characters long geohash, which has an error rate of ±19 meters. 

An example of how the geohash encoder system works here is as follows:

```console
encode(28.1472,84.0823)
'tv5b1k4c'
```

### Geohash Decoder

A geohash decoder converts a geohash into its corresponding tuple of latitude and longitude. 

An example of how the geohash encoder system works here is as follows:

```console
tv5b38vu
{'latitude': 28.173837661743164, 'longitude': 84.0974235534668}
```

### API Docs 

Here is a link to the API docs for geohash encoder decoder: https://geohash-api.herokuapp.com/apidocs/#/default/get_encoder










