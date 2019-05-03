# AuburnHacks19
Hackathon at Auburn University 2019 Project

This project is a combination of Python scripts calling Google Cloud APIs and Ionic Development in Java. We pull information from the Google Geolocation API allowing us to access our current location. Once we have that, we can continually pole the Google Places API to see if we are inside of a hospital. If it turns out that we are in a hospital, we send a pop up notification to the phone asking if you are awake and coherent. If you do not respond to the notification within a set time period, It plays a notification alerting the doctors of your medical condition and sending information to your emergency contacts from a variety of different google APIs.


```
pip install -U googlemaps
pip install responses
pip install python-google-places
sudo apt-get install python-pygame
pip install gTTS
pip install --upgrade google-cloud-translate
```

