# coding=utf-8
import json
from watson_developer_cloud import LanguageTranslatorV2

language_translator = LanguageTranslatorV2(
    username='5d2a9ff3-a1a9-42e7-8e71-ad1cdf8e2875',
    password='GxBmcksgFTI5')


#print(json.dumps(language_translator.get_models(), indent=2))
print(json.dumps(language_translator.get_model('en-ja'), indent=2))


text = "Hello. are you hungry?"

translation = language_translator.translate(
    text,
    source='en',
    target='ja'
    )

print(translation)
