import requests, googlemaps

gmaps = googlemaps.Client(key='AIzaSyC_pk-16CSjVdRBLL9FzIMfkeP0buthiqY')

print (gmaps.geolocate())