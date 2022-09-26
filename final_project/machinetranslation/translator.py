"""
Final python project
"""

import os
#import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = '' #your keys
url = '' #your keys

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    #write the code here
    model_id = 'en-fr'

    french_text = language_translator.translate(
    text=english_text,
    model_id=model_id).get_result()

    return french_text

def french_to_english(french_text):
    #write the code here
    model_id = 'fr-en'

    english_text = language_translator.translate(
    text=french_text,
    model_id=model_id).get_result()

    return english_text
