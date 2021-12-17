import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('OwOqHor4zoTHnHpjPkp0yq9mzJ5qOm-H3L-8NVlieGAp')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/2bae12fa-03c8-402d-97ee-24843cff2a73')

def englishToFrench(englishText):
    frenchText = language_translator.translate(text=englishText,
    model_id='en-fr').get_result()
    return frenchText

def frenchToEnglish(frenchText):
    englishText = language_translator.translate(text=frenchText,
    model_id='fr-en').get_result()
    return englishText

test1 = frenchToEnglish("Bonne")
print(test1)






