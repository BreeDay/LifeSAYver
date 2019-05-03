from gtts import gTTS
import requests

name = "Tyler"
allergies = ["omnicef", "zithromax", "Insulin"]


sentence = "WARNING! WARNING! " + name + " has the following allergies:"

for allergin in allergies:
	sentence = sentence + allergin + " "

number = 0

tts = gTTS(sentence)
path = "audio/" + str(number) + '.mp3'
tts.save(path)

