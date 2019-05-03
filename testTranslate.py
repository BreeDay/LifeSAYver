# Imports the Google Cloud client library
from google.cloud import translate
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/tdoe321/projects/AuburnHacks-3a34beb48439.json"

# Instantiates a client
translate_client = translate.Client()

# The text to translate
text = u'Hello, world!'
# The target language
target = 'es'

# Translates some text into Russian
translation = translate_client.translate(
    text,
    target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))