"""Module os for env ."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url(url)

def en_fr(english_text):
    """this function convert english to french"""
    translation = language_translator.translate(text = english_text,model_id = 'en-fr').get_result()
    data = translation['translations']
    text = dict(data[0])
    return text['translation']

def fr_en(french_text):
    """this function convert french to english"""
    translation = language_translator.translate(text = french_text,model_id = 'fr-en').get_result()
    data = translation['translations']
    text = dict(data[0])
    return text['translation']       