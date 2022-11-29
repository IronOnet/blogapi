import json 
import requests 
from flask import current_app 
from flask_babel import _ 

def translate(text, source_language, target_language): 
    if 'MS_TRANSLATION_KEY' not in current_app.config or not current_app.config['MS_TRANSLATION_KEY']: 
            return _('Error: The translation service is not configured') 

    auth = {
        'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATION_KEY'], 
        'Ocp-Apim-Subscription-Region': 'westus2' }

    r = requests.post(
        'https://api.cognitive.miscrosofttranlator.com' 
        '/translate?api-version=3.0&from={}&to={}'.format(
            source_language, target_language
        ), headers=auth, json=[{'Text': text}]
    )

    if r.status_code != 200: 
        return _('Error: The translation service failed.') 
    return r.json()[0]['Translations'][0]['text'] 