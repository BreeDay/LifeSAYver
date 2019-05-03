from googleplaces import GooglePlaces, types, lang
import sys
import termios
import tty
import os
import time
import requests, googlemaps
from pygame import mixer
from datetime import datetime
from time import gmtime, strftime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import json


import shutil

url = 'https://maps.googleapis.com/maps/api/streetview?size=600x300&location=Emory+Hospital&key=AIzaSyC_pk-16CSjVdRBLL9FzIMfkeP0buthiqY'
response = requests.get(url, stream=True)
with open('img.jpeg', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response